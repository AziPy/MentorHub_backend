from django.db import router

from lessons.views.lesson_views import LessonViewSet

router.register(r'lessons', LessonViewSet)