class Authorization:
    def __init__(self, dao):
        self.dao = dao

    def is_authorized(self, user_id, resource_id, action):
        role_ids = self.dao.get_roles_from_user(user_id)
        accessible_resources = set()
        for role_id in role_ids:
            role_accessible_resources = self.dao.get_resources_from_role_and_access_level(role_id, action)
            accessible_resources = accessible_resources.union(role_accessible_resources)
        if resource_id in accessible_resources:
            return True
        else:
            return False

    def add_role_to_user(self, role_id, user_id):
        self.dao.add_role_to_user(role_id, user_id)

    def remove_user_from_role(self, user_id, role_id):
        self.dao.remove_user_from_role(user_id, role_id)

    def get_all_users(self):
        return self.dao.users

    def get_all_roles(self):
        return self.dao.roles

    def get_all_resources(self):
        return self.dao.resources
