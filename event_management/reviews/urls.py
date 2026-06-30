from django.urls import path
from . import views

urlpatterns = [
    path(
        'add-review/<int:event_id>/',
        views.add_review,
        name='add_review'
    ),
]