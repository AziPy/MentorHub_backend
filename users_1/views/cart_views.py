from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema
from users_1.models import CartItem
from users_1.serializers import CartItemSerializer
from rest_framework.permissions import IsAuthenticated

@extend_schema_view(
    list=extend_schema(
        tags=['Cart'],
        summary='List user users_1 items',
        description='Retrieves users_1 items for the authenticated user.'
    ),
    create=extend_schema(
        tags=['Cart'],
        summary='Add item to users_1',
        description='Adds a course to the user\'s users_1.'
    ),
    retrieve=extend_schema(
        tags=['Cart'],
        summary='Retrieve users_1 item',
        description='Gets a specific users_1 item.'
    ),
    update=extend_schema(
        tags=['Cart'],
        summary='Update users_1 item',
        description='Updates users_1 item quantity.'
    ),
    partial_update=extend_schema(
        tags=['Cart'],
        summary='Partial update users_1 item',
        description='Partially updates users_1 item.'
    ),
    destroy=extend_schema(
        tags=['Cart'],
        summary='Remove users_1 item',
        description='Removes a users_1 item.'
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