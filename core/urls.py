from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pay/', include('payment.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Приложения
    path('api/users/', include('users.urls')),
    path('api/favorites/', include('favorites.urls')),
    path('api/reviews_requests/', include('reviews_requests.urls')),
    path('api/courses/', include('courses_category.urls')),# <- основной путь
]
