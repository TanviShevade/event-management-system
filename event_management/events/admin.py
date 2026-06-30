from django.contrib import admin
from datetime import date
from django.core.mail import send_mail

from .models import Event
from bookings.models import Booking
from payments.models import Payment


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'date',
        'location',
        'available_seats',
        'status'
    )

    actions = [
        'cancel_event'
    ]

    # NEW METHOD
    def save_model(
        self,
        request,
        obj,
        form,
        change
    ):

        # Automatically mark past events as completed
        if obj.date < date.today():
            obj.status = 'completed'

        super().save_model(
            request,
            obj,
            form,
            change
        )

    def has_change_permission(self, request, obj=None):

        if obj is None:
            return True

        if obj.date >= date.today():
            return True

        return False

    def has_delete_permission(self, request, obj=None):

        if obj is None:
            return True

        if obj.date >= date.today():
            return True

        return False

    def cancel_event(self, request, queryset):

        for event in queryset:

            event.status = 'cancelled'
            event.save()

            bookings = Booking.objects.filter(
                event=event,
                status='confirmed'
            )

            for booking in bookings:

                booking.status = 'cancelled'
                booking.save()

                try:

                    payment = Payment.objects.get(
                        booking=booking
                    )

                    payment.status = 'Refunded'
                    payment.save()

                except Payment.DoesNotExist:
                    pass

                if booking.user.email:

                    send_mail(

                        subject='Event Cancelled',

                        message=f'''
Dear {booking.user.username},

We regret to inform you that the following event has been cancelled.

Event: {event.title}
Date: {event.date}
Location: {event.location}

Your booking has been cancelled.

Your payment has been marked as refunded.

Thank you for using Event Management System.
''',

                        from_email=None,

                        recipient_list=[
                            booking.user.email
                        ],

                        fail_silently=True
                    )

        self.message_user(
            request,
            "Selected events cancelled successfully and users notified."
        )

    cancel_event.short_description = (
        "Cancel selected events and refund users"
    )