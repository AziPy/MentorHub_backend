from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema
from users.models import Review
from users.serializers import ReviewSerializer

@extend_schema_view(
    list=extend_schema(tags=['Reviews']),
    retrieve=extend_schema(tags=['Reviews']),
    create=extend_schema(tags=['Reviews']),
    update=extend_schema(tags=['Reviews']),
    partial_update=extend_schema(tags=['Reviews']),
    destroy=extend_schema(tags=['Reviews']),
)
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if not hasattr(request.user, 'role') or request.user.role != 'student':
            return Response({"error": "Only students can create reviews"}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
