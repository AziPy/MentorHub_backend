from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema
from users.models import Lesson
from users.serializers import LessonSerializer
from users.permissions import CanCreateEditCourse
from rest_framework.exceptions import PermissionDenied


@extend_schema_view(
    list=extend_schema(tags=['Lessons']),
    retrieve=extend_schema(tags=['Lessons']),
    create=extend_schema(tags=['Lessons']),
    update=extend_schema(tags=['Lessons']),
    partial_update=extend_schema(tags=['Lessons']),
    destroy=extend_schema(tags=['Lessons']),
)
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [CanCreateEditCourse]

    def perform_create(self, serializer):
        if self.request.user.role in ['mentor', 'admin']:
            # Serializer handles course FK automatically from data
            serializer.save()
        else:
            raise PermissionDenied("Only mentors and admins can create lessons")