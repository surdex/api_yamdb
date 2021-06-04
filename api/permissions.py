from rest_framework import permissions


class IsAuthAdmModerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        result = (
            request.method in permissions.SAFE_METHODS
            or request.user == obj.author
            or request.user.role == 'moderator'
            or request.user.role == 'admin'
        )
        return result


class DoWhatYouWant(permissions.BasePermission):
    def has_permission(self, request, view):
        return True


class AdminOnly(permissions.BasePermission):
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
