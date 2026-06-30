from django.urls import path
from . import views

urlpatterns = [

    path(
        'pay/<int:booking_id>/',
        views.make_payment,
        name='make_payment'
    ),

    path(
        'success/<int:booking_id>/',
        views.payment_success,
        name='payment_success'
    ),

    path(
        'transactions/',
        views.transaction_history,
        name='transaction_history'
    ),

]