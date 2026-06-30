from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:event_id>/', views.book_event, name='book_event'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
   path(
    'cancel/<int:booking_id>/',
    views.cancel_booking,
    name='cancel_booking'
),
]