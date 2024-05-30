from django.contrib.auth import get_user_model
from rest_framework import permissions


class IsAuthorOrIsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser or request.user.role != get_user_model().MANAGER:
            return True

        return False

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser or request.user.role == get_user_model().ADMIN:
            return True

        try:
            if obj.user == request.user:
                return True
        except AttributeError:
            ...

        try:
            if obj.book.user == request.user:
                return True
        except AttributeError:
            ...

        return False
