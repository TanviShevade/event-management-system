from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Booking(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    # Number of seats booked
    quantity = models.PositiveIntegerField(
        default=1
    )

    booked_at = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):

        return (
            f"{self.user.username} - "
            f"{self.event.title} "
            f"({self.quantity} seat(s))"
        )