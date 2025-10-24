from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from payment.models import Order
import requests
from django.conf import settings

NOWPAYMENTS_API_KEY = settings.NOWPAYMENTS_API_KEY
BASE_URL = "https://api.nowpayments.io/v1"

@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('order_id', openapi.IN_PATH, description="ID заказа", type=openapi.TYPE_INTEGER)
    ],
    responses={200: "JSON с invoice_url"}
)
@api_view(['GET'])
def create_payment(request, order_id):
    order = Order.objects.get(id=order_id)
    payload = {
        "price_amount": float(order.amount_usd),
        "price_currency": "usd",
        "pay_currency": "btc",
        "order_id": str(order.id),
        "ipn_callback_url": "https://yourdomain.com/api/payment/webhook/"
    }
    headers = {"x-api-key": NOWPAYMENTS_API_KEY}
    response = requests.post(f"{BASE_URL}/payment", json=payload, headers=headers)
    data = response.json()
    order.payment_id = data.get("payment_id")
    order.save()
    return Response({"invoice_url": data.get("invoice_url")})

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'payment_id': openapi.Schema(type=openapi.TYPE_STRING),
            'payment_status': openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
    responses={200: "OK"}
)
@api_view(['POST'])
def payment_webhook(request):
    data = request.data
    payment_id = data.get("payment_id")
    payment_status = data.get("payment_status")
    order = Order.objects.filter(payment_id=payment_id).first()
    if not order:
        return Response({"error": "Order not found"}, status=404)
    order.status = payment_status
    order.save()
    return Response({"message": "ok"})
