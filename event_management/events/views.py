from django.shortcuts import render
from datetime import date
from .models import Event


def home(request):
    return render(request, 'home.html')


def event_list(request):

    category = request.GET.get('category')

    upcoming_events = Event.objects.filter(
        date__gte=date.today()
    )

    if category:
        upcoming_events = upcoming_events.filter(
            category=category
        )

    past_events = Event.objects.filter(
        date__lt=date.today()
    )

    return render(request, 'event_list.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    })