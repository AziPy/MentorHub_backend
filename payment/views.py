from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from .models import Order
from .serializers import (
    OrderSerializer,
    CreateOrderSerializer,
    PaymentWebhookSerializer
)

YOUR_WALLET_ADDRESS = "0xD64Bd94Fd4f5bE3711746080855D968a40dE62F1"


@extend_schema(
    request=CreateOrderSerializer,
    responses={201: OrderSerializer},
    examples=[
        OpenApiExample(
            "Пример запроса",
            summary="Создание нового заказа",
            value={"amount_usd": "10.00"},
        )
    ],
)
@api_view(['POST'])
def create_order(request):

    serializer = CreateOrderSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    order = Order.objects.create(amount_usd=serializer.validated_data['amount_usd'])
    return Response(OrderSerializer(order).data, status=201)



@extend_schema(
    responses={
        200: OpenApiResponse(
            description="Возвращает адрес кошелька и сумму для перевода",
            examples=[
                OpenApiExample(
                    "Пример ответа",
                    value={
                        "wallet_address": YOUR_WALLET_ADDRESS,
                        "amount_usd": "10.00",
                        "order_id": 1,
                    },
                )
            ],
        )
    }
)
@api_view(['GET'])
def create_payment(request, order_id):

    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)

    return Response({
        "wallet_address": YOUR_WALLET_ADDRESS,
        "amount_usd": str(order.amount_usd),
        "order_id": order.id,
    })




@extend_schema(
    request=PaymentWebhookSerializer,
    responses={
        200: OpenApiResponse(
            description="Отмечает заказ как оплаченный",
            examples=[
                OpenApiExample(
                    "Пример запроса",
                    value={"order_id": 1, "tx_hash": "0x123abc456def"},
                ),
                OpenApiExample(
                    "Пример ответа",
                    value={"message": "Payment recorded"},
                ),
            ],
        )
    },
)
@api_view(['POST'])
def payment_webhook(request):
    serializer = PaymentWebhookSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    order_id = serializer.validated_data['order_id']

    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)

    order.status = "paid"
    order.save()

    return Response({"message": "Payment recorded"}, status=200)
