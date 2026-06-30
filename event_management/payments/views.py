from django.shortcuts import (
    render,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import EmailMessage

from bookings.models import Booking
from .models import Payment

from io import BytesIO
from reportlab.pdfgen import canvas

import random


def make_payment(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    if Payment.objects.filter(
        booking=booking
    ).exists():

        payment = Payment.objects.get(
            booking=booking
        )

        return render(
            request,
            'payment_success.html',
            {
                'booking': booking,
                'payment': payment,
                'message': 'Payment already completed.'
            }
        )

    amount = booking.quantity * 500

    return render(
        request,
        'payment.html',
        {
            'booking': booking,
            'amount': amount
        }
    )


def payment_success(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    if not Payment.objects.filter(
        booking=booking
    ).exists():

        transaction_id = "TXN" + str(
            random.randint(100000, 999999)
        )

        Payment.objects.create(
            booking=booking,
            user=request.user,
            amount=booking.quantity * 500,
            transaction_id=transaction_id,
            status='Paid'
        )

        # Create PDF Ticket
        buffer = BytesIO()

        p = canvas.Canvas(buffer)

        p.setFont(
            "Helvetica-Bold",
            16
        )

        p.drawString(
            200,
            800,
            "EVENT TICKET"
        )

        p.line(
            50,
            780,
            550,
            780
        )

        p.setFont(
            "Helvetica",
            12
        )

        p.drawString(
            50,
            740,
            f"Event : {booking.event.title}"
        )

        p.drawString(
            50,
            710,
            f"User : {request.user.username}"
        )

        p.drawString(
            50,
            680,
            f"Booking ID : {booking.id}"
        )

        p.drawString(
            50,
            650,
            f"Transaction ID : {transaction_id}"
        )

        p.drawString(
            50,
            620,
            f"Seats : {booking.quantity}"
        )

        p.drawString(
            50,
            590,
            f"Amount : ₹{booking.quantity * 500}"
        )

        p.showPage()
        p.save()

        buffer.seek(0)

        email = EmailMessage(

            subject='Booking Confirmed',

            body=f'''
Hello {request.user.username},

Your booking has been confirmed.

Event : {booking.event.title}

Seats : {booking.quantity}

Transaction ID : {transaction_id}

Amount : ₹{booking.quantity * 500}

Ticket PDF is attached.

Thank you for using Event Management System.
''',

            from_email=settings.EMAIL_HOST_USER,

            to=[request.user.email]

        )

        email.attach(
            f'ticket_{booking.id}.pdf',
            buffer.getvalue(),
            'application/pdf'
        )

        email.send()

        booking.status = 'confirmed'
        booking.save()

        # Deduct seats
        booking.event.available_seats -= booking.quantity
        booking.event.save()

    payment = Payment.objects.get(
        booking=booking
    )

    return render(
        request,
        'payment_success.html',
        {
            'booking': booking,
            'payment': payment
        }
    )


@login_required
def transaction_history(request):

    payments = Payment.objects.filter(
        user=request.user
    ).order_by(
        '-paid_at'
    )

    return render(
        request,
        'transaction_history.html',
        {
            'payments': payments
        }
    )