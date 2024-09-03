from rest_framework import permissions

from django.contrib.auth import get_user_model


CustomUser = get_user_model()

class IsSaler(permissions.BasePermission):
    """
    Allows access only to users with the 'Saler' role.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role.title == 'Saler'


class IsSimpleUser(permissions.BasePermission):
    """
    Allows access only to users with the 'SimpleUser' role.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role.title == 'SimpleUser'