from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date

from .models import Review
from .forms import ReviewForm
from events.models import Event
from bookings.models import Booking


@login_required
def add_review(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    # Event must be over
    if event.date >= date.today():
        return redirect('home')

    # User must have booked event
    booked = Booking.objects.filter(
        user=request.user,
        event=event,
        status='confirmed'
    ).exists()

    if not booked:
        return redirect('home')

    # One review only
    existing_review = Review.objects.filter(
        user=request.user,
        event=event
    ).exists()

    if existing_review:
        return redirect('home')

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)
            review.user = request.user
            review.event = event
            review.save()

            return redirect('home')

    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {
        'form': form,
        'event': event
    })