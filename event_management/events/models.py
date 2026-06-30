from django.db import models


CATEGORY_CHOICES = [
    ('Concerts & Live Music Performances', 'Concerts & Live Music Performances'),
    ('Corporate & Business Events', 'Corporate & Business Events'),
    ('Social & Private Events', 'Social & Private Events'),
    ('Community & Cultural Events', 'Community & Cultural Events'),
    ('Sports & Wellness', 'Sports & Wellness'),
    ('Educational & Workshop Events', 'Educational & Workshop Events'),
]


STATUS_CHOICES = (
    ('upcoming', 'Upcoming'),
    ('cancelled', 'Cancelled'),
)


class Event(models.Model):

    title = models.CharField(
        max_length=200
    )

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default='Concerts & Live Music Performances'
    )

    date = models.DateField()

    location = models.CharField(
        max_length=200
    )

    available_seats = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='upcoming'
    )

    def __str__(self):
        return self.title