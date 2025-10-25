# payment/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer, CreateOrderSerializer, PaymentWebhookSerializer
from drf_yasg.utils import swagger_auto_schema

YOUR_WALLET_ADDRESS = "0xD64Bd94Fd4f5bE3711746080855D968a40dE62F1"

@swagger_auto_schema(method='post', request_body=CreateOrderSerializer, responses={201: OrderSerializer})
@api_view(['POST'])
def create_order(request):
    serializer = CreateOrderSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    order = Order.objects.create(amount_usd=serializer.validated_data['amount_usd'])
    return Response(OrderSerializer(order).data, status=201)


@api_view(['GET'])
def create_payment(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)

    return Response({
        "wallet_address": YOUR_WALLET_ADDRESS,
        "amount_usd": str(order.amount_usd),
        "order_id": order.id
    })


@swagger_auto_schema(method='post', request_body=PaymentWebhookSerializer)
@api_view(['POST'])
def payment_webhook(request):
    serializer = PaymentWebhookSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    order_id = serializer.validated_data['order_id']

    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)

    order.status = "paid"
    order.save()
    return Response({"message": "Payment recorded"})
