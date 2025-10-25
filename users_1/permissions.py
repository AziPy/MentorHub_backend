from rest_framework import permissions

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