from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Сначала проверяем аутентификацию
        if not request.user or not request.user.is_authenticated:
            return False

        # Затем проверяем роль для не-GET методов
        if request.method in permissions.SAFE_METHODS:
            return True

        # Строгая проверка роли админа
        return hasattr(request.user, 'role') and request.user.role == 'admin'
class IsAdminUser(permissions.BasePermission):
    """
    Разрешает доступ только админам.
    """
    def has_permission(self, request, view):
        return (request.user and
                request.user.is_authenticated and
                hasattr(request.user, 'role') and
                request.user.role == 'admin')

class IsMentorOrAdmin(permissions.BasePermission):
    """Разрешает доступ менторам и админам"""
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        return (hasattr(request.user, 'role') and
                request.user.role in ['mentor', 'admin'])

class CanCreateEditCourse(permissions.BasePermission):
    """Разрешает создание/редактирование курсов менторам и админам"""
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        # GET запросы разрешены всем аутентифицированным
        if request.method in permissions.SAFE_METHODS:
            return True

        # Создание/редактирование только менторам и админам
        return (hasattr(request.user, 'role') and
                request.user.role in ['mentor', 'admin'])

class IsMentor(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and request.user.role == 'mentor')

from rest_framework.permissions import BasePermission, SAFE_METHODS

class CartPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False  # анонимам доступ запрещен

        # Админ может со всеми
        if request.user.is_superuser:
            return True

        # Ментор не имеет доступа к корзине
        if getattr(request.user, 'role', None) == 'mentor':
            return False

        # Студент может работать со своей корзиной
        if getattr(request.user, 'role', None) == 'student':
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        # Студент может только со своими объектами
        if getattr(request.user, 'role', None) == 'student' and obj.user == request.user:
            return True

        return False

from rest_framework.permissions import BasePermission, SAFE_METHODS

class MentorPermission(BasePermission):
    """
    Просмотр доступен всем, изменение только для админа
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_superuser
