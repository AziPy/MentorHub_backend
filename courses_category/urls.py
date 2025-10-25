from rest_framework.routers import DefaultRouter
from django.urls import path, include
from courses_category.views.category_views import CategoryViewSet
from courses_category.views.course_views import CourseViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router.urls)),
]
