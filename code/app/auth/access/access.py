from flask import g
from app.models.role import RoleEnum
from app.models.permission import PermissionEnum
from .exceptions import UserIsNotPermitted


class AccessManager(object):

    @staticmethod
    def user_is_role(role_name):
        if isinstance(role_name, RoleEnum):
            role_name = role_name.value
        return role_name == g.user.role.name

    @staticmethod
    def user_has_permission(permission_name):
        if isinstance(permission_name, PermissionEnum):
            permission_name = permission_name.value
        return permission_name in [p.name for p in g.user.role.permissions]

    @staticmethod
    def check_user_has_permission_on(user, target_permission_other,
                                     target_permission_self=None):
        '''
        Given a user, check if the current user has a permission on it.
        The user supplied may be the current user or another user.
        Used in situations where a user owns something, but it may be
        modified by another user with sufficient roles/permissions.

        If it is the current user (self), we simply check if the user has
        the permission (target_permission_self).

        Otherwise (other) we check if the user has the permission
        (target_permission_other) on another user and if the current user
        role is greater.
        '''
        if user.id == g.user.id:
            if not AccessManager.user_has_permission(target_permission_self):
                raise UserIsNotPermitted
        else:
            if (not AccessManager.user_has_permission(target_permission_other)
                or not AccessManager.user_role_is_greater(g.user, user)):
                raise UserIsNotPermitted

    @staticmethod
    def user_role_is_greater(user, other_user):
        '''
        Checks if a user has a greater role than another
        '''
        return role_is_greater(user.role, other_user.role)

    @staticmethod
    def role_is_greater(role_name, other_role_name):
        '''
        Check if one role is greater than another

        Example:
            ADMIN > GUEST
        '''
        roles_with_levels = {v: k for k, v in enumerate(list(RoleEnum)[::-1])}
        return roles_with_levels[role_name] > roles_with_levels[other_role_name]
