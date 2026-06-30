from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from .forms import BookingForm
from .models import Booking

from events.models import Event
from payments.models import Payment

from datetime import date


def book_event(request, event_id):

    event = get_object_or_404(
        Event,
        id=event_id
    )

    # Prevent booking past events
    if event.date < date.today():
        return redirect('home')

    # Login required
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':

        quantity = int(
            request.POST.get('quantity')
        )

        # Seat validation
        if quantity > event.available_seats:

            return render(
                request,
                'book_event.html',
                {
                    'event': event,
                    'error': 'Not enough seats available'
                }
            )

        booking = Booking.objects.create(
            user=request.user,
            event=event,
            quantity=quantity,
            status='pending'
        )

        return redirect(
            'make_payment',
            booking.id
        )

    return render(
        request,
        'book_event.html',
        {
            'event': event
        }
    )


@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by(
        '-booked_at'
    )

    return render(
        request,
        'my_bookings.html',
        {
            'bookings': bookings
        }
    )


@login_required
def cancel_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    if booking.status == 'confirmed':

        booking.status = 'cancelled'
        booking.save()

        # Restore seats
        booking.event.available_seats += booking.quantity
        booking.event.save()

        try:

            payment = Payment.objects.get(
                booking=booking
            )

            payment.status = 'Cancelled'
            payment.save()

        except Payment.DoesNotExist:
            pass

    return redirect(
        'my_bookings'
    )