from django.urls import path
from . import views

urlpatterns = [
    path('create-order/', views.create_order, name='create_order'),

    path('create-payment/<int:order_id>/', views.create_payment, name='create_payment'),

    path('payment/webhook/', views.payment_webhook, name='payment_webhook'),
]
