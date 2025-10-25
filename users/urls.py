from django.db import router
from django.urls import path, include

from users.views.auth_views import RegisterView, LoginView

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
]