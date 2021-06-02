from rest_framework.permissions import BasePermission


class DoWhatYouWant(BasePermission):
    def has_permission(self, request, view):
        return True