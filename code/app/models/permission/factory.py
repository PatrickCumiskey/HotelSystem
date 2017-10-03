from .permission import Permission, PermissionEnum


class PermissionFactory(object):
    '''
    Gets a Permission that corresponds to a Permission enum/string but creates it
    if it doesn't exist.

    Defers creation and localises the retrival and creation of a Permission.
    '''
    @staticmethod
    def get_permission(permission_enum):
        permission = Permission.query.filter_by(name=permission_enum.value).first()
        if permission is not None:
            return permission
        if permission_enum in PermissionEnum:
            return Permission(name=permission_enum.value)
        raise ValueError('{} is not a valid permission'.format(permission_enum))
