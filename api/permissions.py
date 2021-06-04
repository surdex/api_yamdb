
from rest_framework import permissions


class IsUserIsAdmin(permissions.BasePermission):
    def has_permisson(self, request, view):
        if request.user.is_authenticated and (
                request.user.is_superuser or request.user.role == 'admin'
        ):
            return True
        else:
            return False

    def has_object_permisson(self, request, view, obj):
        pass


class IsUserIsAdmin2(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser or request.user.role == 'admin'