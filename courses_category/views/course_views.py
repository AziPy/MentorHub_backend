from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema_view, extend_schema
from users.models import Course
from users.permissions import CanCreateEditCourse
from .serializers import CourseSerializer

@extend_schema_view(
    list=extend_schema(tags=['Courses']),
    retrieve=extend_schema(tags=['Courses']),
    create=extend_schema(tags=['Courses']),
    update=extend_schema(tags=['Courses']),
    partial_update=extend_schema(tags=['Courses']),
    destroy=extend_schema(tags=['Courses']),
)
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [CanCreateEditCourse]

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.query_params.get('sort', 'date')
        if sort == 'price':
            return queryset.order_by('price')
        elif sort == 'rating':
            return queryset.order_by('-rating')
        return queryset.order_by('-created_at')

    def perform_create(self, serializer):
        if self.request.user.role in ['mentor', 'admin']:
            serializer.save(mentor=self.request.user)
        else:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only mentors and admins can create courses")