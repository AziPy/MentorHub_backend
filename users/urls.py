from rest_framework.routers import DefaultRouter
from django.urls import path, include
from users.views.cart_views import CartViewSet
from users.views.auth_views import RegisterView, LoginView, LogoutView
from users.views.profile_views import UserProfileView

router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
