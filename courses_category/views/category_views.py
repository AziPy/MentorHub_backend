from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_spectacular.utils import extend_schema_view, extend_schema
from users_1.models import Category
from users_1.permissions import IsAdminOrReadOnly
from users_1.serializers import CategorySerializer

@extend_schema_view(
    list=extend_schema(tags=['Categories']),
    retrieve=extend_schema(tags=['Categories']),
    create=extend_schema(tags=['Categories']),
    update=extend_schema(tags=['Categories']),
    partial_update=extend_schema(tags=['Categories']),
    destroy=extend_schema(tags=['Categories']),
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
