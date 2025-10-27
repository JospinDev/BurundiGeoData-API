from rest_framework import permissions

class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
    Permission rules:
    - Anyone (even anonymous) can read (GET, HEAD, OPTIONS)
    - Only superusers can create, update or delete
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_authenticated and request.user.is_superuser
