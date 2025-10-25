from rest_framework import permissions

class IsMentor(permissions.BasePermission):
    """
    Allows access only to reviews_requests with role 'mentor'.
    """
    def has_permission(self, request, view):
        return hasattr(request.user, 'userprofile') and request.user.userprofile.role == 'mentor'
    def has_object_permission(self, request, view, obj):
        return hasattr(request.user, 'userprofile') and request.user.userprofile.role == 'mentor'