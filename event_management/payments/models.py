from django.db import models
from django.contrib.auth.models import User
from bookings.models import Booking


PAYMENT_STATUS_CHOICES = (
    ('Paid', 'Paid'),
    ('Refunded', 'Refunded'),
    ('Cancelled', 'Cancelled'),
)


class Payment(models.Model):

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    transaction_id = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default='Paid'
    )

    paid_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return str(self.transaction_id)