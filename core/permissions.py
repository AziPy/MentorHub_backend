# core/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class ReadOnlyOrAuthenticated(BasePermission):
    """
    Разрешает доступ для всех только на "безопасные" методы (GET, HEAD, OPTIONS),
    а для изменений (POST, PUT, PATCH, DELETE) требует аутентификацию.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
