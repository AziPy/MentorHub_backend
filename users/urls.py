from django.db import router

from users.views.favorite_views import FavoriteViewSet

router.register(r'favorites', FavoriteViewSet,