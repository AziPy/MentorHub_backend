from rest_framework.permissions import BasePermission, SAFE_METHODS

class CoursePermission(BasePermission):
    """
    Чтение доступно всем.
    Создание/изменение/удаление только для админа.
    """
    def has_permission(self, request, view):
        # Все GET запросы разрешены
        if request.method in SAFE_METHODS:
            return True

        # Для остальных методов нужен авторизованный админ
        return request.user.is_authenticated and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        # Чтение всем
        if request.method in SAFE_METHODS:
            return True

        # Изменение/удаление только админ
        return request.user.is_authenticated and request.user.is_superuser
