from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema
from users.models import CartItem
from users.serializers import CartItemSerializer
from rest_framework.permissions import IsAuthenticated

@extend_schema_view(
    list=extend_schema(
        tags=['Cart'],
        summary='List user cart items',
        description='Retrieves cart items for the authenticated user.'
    ),
    create=extend_schema(
        tags=['Cart'],
        summary='Add item to cart',
        description='Adds a course to the user\'s cart.'
    ),
    retrieve=extend_schema(
        tags=['Cart'],
        summary='Retrieve cart item',
        description='Gets a specific cart item.'
    ),
    update=extend_schema(
        tags=['Cart'],
        summary='Update cart item',
        description='Updates cart item quantity.'
    ),
    partial_update=extend_schema(
        tags=['Cart'],
        summary='Partial update cart item',
        description='Partially updates cart item.'
    ),
    destroy=extend_schema(
        tags=['Cart'],
        summary='Remove cart item',
        description='Removes a cart item.'
    )
)
class CartViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)