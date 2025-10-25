from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views.review_views import ReviewViewSet
from users.views.requests_views import RequestsNewViewSet

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'requests', RequestsNewViewSet, basename='requests')

urlpatterns = [
    path('', include(router.urls)),
]
