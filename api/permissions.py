from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        result = (
            request.method in permissions.SAFE_METHODS
            or request.user == obj.author
        )
        return result
