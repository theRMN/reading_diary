from rest_framework import permissions
from django.contrib.auth import get_user_model


class IsAdminOrIsModer(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.role != get_user_model().USER:
                return True

            if obj == request.user:
                return True

        return False
