from rest_framework.routers import DefaultRouter
from django.urls import path, include
from favorites.views.favorite_views import FavoriteViewSet

router = DefaultRouter()
router.register(r'favorites', FavoriteViewSet, basename='favorites')

urlpatterns = [
    path('', include(router.urls)),
]
