from django.db import router

from courses_category.views.category_views import CategoryViewSet
from courses_category.views.course_views import CourseViewSet

router.register(r'categories', CategoryViewSet)
router.register(r'courses', CourseViewSet)