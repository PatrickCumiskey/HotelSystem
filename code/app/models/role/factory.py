from .role import Role, RoleEnum
from app.models.permission import PermissionFactory
from app.models.permission import PermissionEnum as P


class RoleFactory(object):
    '''
    Gets a role that corresponds to a role enum/string but creates it
    if it doesn't exist.

    Defers creation and localises the retrival and creation of a Role.
    '''
    # Note: part of the building process is actually handled by the ORM
    @staticmethod
    def get_role(role_enum):
        role = Role.query.filter_by(name=role_enum.value).first()
        if role is not None:
            # existing / non default roles
            return role
        if role_enum in RoleEnum:
            role = Role(name=role_enum.value)
            role.permissions = RoleFactory._get_default_permissions(role_enum)
            return role
        raise ValueError('{} is not a valid role'.format(role_enum))

    @staticmethod
    def _get_default_permissions(role_enum):
        # factor out (business logic)?
        # external config?
        options = {
            RoleEnum.ADMIN:     [],
            RoleEnum.MANAGER:   [P.VIEW_OTHER_USER, P.CREATE_OTHER_USER, P.EDIT_OTHER_USER, P.DELETE_OTHER_USER,
                                 P.VIEW_OTHERS_BOOKING, P.MAKE_OTHERS_BOOKING, P.EDIT_OTHERS_BOOKING, P.CANCEL_OTHERS_BOOKING],
            RoleEnum.STAFF:     [P.VIEW_OTHERS_BOOKING, P.MAKE_OTHERS_BOOKING, P.EDIT_OTHERS_BOOKING, P.CANCEL_OTHERS_BOOKING],
            RoleEnum.GUEST:     [P.VIEW_USER, P.EDIT_USER, P.DELETE_USER],
            RoleEnum.ANONYMOUS: [P.CREATE_USER]
        }
        if role_enum in options:
            return list(map(PermissionFactory.get_permission, options[role_enum]))
        else:
            return []
