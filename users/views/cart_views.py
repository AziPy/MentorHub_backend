from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema
from users.models import CartItem
from users.serializers import CartItemSerializer
from rest_framework.permissions import IsAuthenticated

@extend_schema_view(
    list=extend_schema(
        tags=['Cart'],
        summary='List user users items',
        description='Retrieves users items for the authenticated user.'
    ),
    create=extend_schema(
        tags=['Cart'],
        summary='Add item to users',
        description='Adds a course to the user\'s users.'
    ),
    retrieve=extend_schema(
        tags=['Cart'],
        summary='Retrieve users item',
        description='Gets a specific users item.'
    ),
    update=extend_schema(
        tags=['Cart'],
        summary='Update users item',
        description='Updates users item quantity.'
    ),
    partial_update=extend_schema(
        tags=['Cart'],
        summary='Partial update users item',
        description='Partially updates users item.'
    ),
    destroy=extend_schema(
        tags=['Cart'],
        summary='Remove users item',
        description='Removes a users item.'
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