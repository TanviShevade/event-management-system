from django.shortcuts import render
from bookings.models import Booking
from events.models import Event
from datetime import date

def dashboard(request):

    total_bookings = Booking.objects.filter(
    user=request.user,
    status='confirmed'
).count()
    upcoming_events = Event.objects.filter(
        date__gte=date.today()
    ).count()

    recent_bookings = Booking.objects.filter(
    user=request.user,
    status='confirmed'
).order_by('-booked_at')[:5]

    context = {
        'total_bookings': total_bookings,
        'upcoming_events': upcoming_events,
        'recent_bookings': recent_bookings,
    }

    return render(request, 'dashboard.html', context)