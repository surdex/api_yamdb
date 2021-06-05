from rest_framework import permissions


class IsUserIsAdmin(permissions.BasePermission):
    message = 'The user must have the admin status!'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.role == 'admin'
