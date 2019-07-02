class User:
    def __init__(self, record):
        self.id = record.get('id')
        self.name = record.get('name')

    def __str__(self):
        return 'id: {}, name: {}'.format(self.id, self.name)


class Resource:
    def __init__(self, record):
        self.id = record.get('id')
        self.name = record.get('name')

    def __str__(self):
        return 'id: {}, name: {}'.format(self.id, self.name)


class Role:
    def __init__(self, record):
        self.id = record.get('id')
        self.name = record.get('name')

    def __str__(self):
        return 'id: {}, name: {}'.format(self.id, self.name)


class UserRoleRelation:
    def __init__(self, record):
        self.user_id = record.get('user_id')
        self.role_id = record.get('role_id')


class RoleResourceRelation:
    def __init__(self, record):
        self.role_id = record.get('role_id')
        self.resource_id = record.get('resource_id')
        self.access_level = record.get('access_level')
