from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('events.urls')),
    path('book/', include('bookings.urls')),
    path('bookings/', include('bookings.urls')),
    path('users/', include('users.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('reviews/', include('reviews.urls')),
    path('admin-dashboard/', include('admin_dashboard.urls')),
    path('payments/', include('payments.urls')),
    path(
    'tickets/',
    include('tickets.urls')
),
 path('', include('pages.urls')),
]