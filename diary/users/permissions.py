from rest_framework import permissions
from django.contrib.auth import get_user_model


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == get_user_model().ADMIN
        return False
