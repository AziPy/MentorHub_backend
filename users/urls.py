from django.db import router

from users.views.cart_views import CartViewSet

router.register(r'cart', CartViewSet)