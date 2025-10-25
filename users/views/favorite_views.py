from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.models import Favorite
from users.serializers import FavoriteSerializer

@extend_schema_view(
    list=extend_schema(
        tags=['Favorites'],
        summary='List user favorites',
        description='Retrieves favorites for the authenticated user.'
    ),
    create=extend_schema(
        tags=['Favorites'],
        summary='Add to favorites',
        description='Adds course or mentor to favorites.'
    ),
    retrieve=extend_schema(
        tags=['Favorites'],
        summary='Retrieve favorite',
        description='Gets a specific favorite.'
    ),
    update=extend_schema(
        tags=['Favorites'],
        summary='Update favorite',
        description='Updates favorite (rarely used).'
    ),
    partial_update=extend_schema(
        tags=['Favorites'],
        summary='Partial update favorite',
        description='Partially updates favorite.'
    ),
    destroy=extend_schema(
        tags=['Favorites'],
        summary='Remove from favorites',
        description='Removes from favorites.'
    )
)


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)