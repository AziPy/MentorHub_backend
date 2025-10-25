# payment/serializers.py
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'amount_usd', 'payment_id', 'status']
        read_only_fields = ['id', 'payment_id', 'status']


class CreateOrderSerializer(serializers.Serializer):
    amount_usd = serializers.DecimalField(
        max_digits=10, decimal_places=2, min_value=0.01
    )


class PaymentWebhookSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    tx_hash = serializers.CharField(max_length=255)
