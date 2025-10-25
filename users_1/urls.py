from django.db import router
from django.urls import path, include

from users_1.views.cart_views import CartViewSet
from users_1.views.auth_views import RegisterView, LoginView, LogoutView
from users_1.views.profile_views import UserProfileView

router.register(r'cart', CartViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]