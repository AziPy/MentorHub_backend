# reviews/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReviewPermission(BasePermission):
    def has_permission(self, request, view):
        # GET разрешаем всем
        if request.method in SAFE_METHODS:
            return True

        # Если пользователь не авторизован — запрет
        if not request.user.is_authenticated:
            return False

        # Админ может всё
        if request.user.is_superuser:
            return True

        # Ментор может только читать (SAFE_METHODS), но не писать
        if getattr(request.user, 'role', None) == 'mentor':
            return False

        # Студент может делать POST/PUT/DELETE для своих объектов (проверка на объекте)
        return True

    def has_object_permission(self, request, view, obj):
        # Чтение всем
        if request.method in SAFE_METHODS:
            return True

        if not request.user.is_authenticated:
            return False

        # Админ может всё
        if request.user.is_superuser:
            return True

        # Ментор не может менять
        if getattr(request.user, 'role', None) == 'mentor':
            return False

        # Студент может менять только свои объекты
        if getattr(request.user, 'role', None) == 'student' and obj.user == request.user:
            return True

        return False

from rest_framework.permissions import BasePermission, SAFE_METHODS

class RequestPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        role = getattr(request.user, 'role', None)
        if request.user.is_superuser:
            return True  # админ видит всё
        if role == 'mentor':
            return True  # ментор может работать со своими объектами
        return False  # студенты и анонимы не имеют доступа

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        role = getattr(request.user, 'role', None)
        if request.user.is_superuser:
            return True  # админ может со всеми
        if role == 'mentor' and obj.user == request.user:
            return True  # ментор только со своими
        return False  # студенты и анонимы не могут

