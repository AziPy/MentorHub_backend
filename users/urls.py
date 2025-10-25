from django.db import router

from users.views.lesson_views import LessonViewSet

router.register(r'lessons', LessonViewSet)