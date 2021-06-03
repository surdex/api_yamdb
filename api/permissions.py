from rest_framework.permissions import BasePermission


class DoWhatYouWant(BasePermission):
    def has_permission(self, request, view):
        return True


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and (
            request.user.is_superuser or request.user.role == 'admin'
        ):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and (
            request.user.is_superuser or request.user.role == 'admin'
        ):
            return True
        return False
