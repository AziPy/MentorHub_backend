from django.db import router

from favorites.views.favorite_views import FavoriteViewSet

router.register(r'favorites', FavoriteViewSet,