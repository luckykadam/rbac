import csv

from models import User, Resource, Role, UserRoleRelation, RoleResourceRelation
from exceptions import UnknownUser, UnknownRole, UnknownAccessLevel, UserNotAssignedToRole
from utils import access_levels


class DataAccessObject:

    def __init__(self):
        self.users = {}
        self.resources = {}
        self.roles = {}
        self.user_to_roles = {}
        self.role_to_resources = {}

    def load_data(self):
        print('loading users')
        with open('data/users.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                user = User(row)
                self.users[user.id] = user
        # print(self.users)

        print('loading resources')
        with open('data/resources.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                resource = Resource(row)
                self.resources[resource.id] = resource
        # print(self.resources)

        print('loading roles')
        with open('data/roles.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                role = Role(row)
                self.roles[role.id] = role
        # print(self.roles)

        print('loading user_role_relations')
        self.user_to_roles = {user_id: set() for user_id in self.users}
        with open('data/user_role_relations.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                user_role_relation = UserRoleRelation(row)
                self.user_to_roles[user_role_relation.user_id].add(user_role_relation.role_id)
        # print(self.user_to_roles)

        print('loading role_resource_relations')
        self.role_to_resources = {user_id: {access_level: set() for access_level in access_levels} for user_id in self.users}
        with open('data/role_resource_relations.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                role_resource_relation = RoleResourceRelation(row)
                self.role_to_resources[role_resource_relation.role_id][role_resource_relation.access_level].add(role_resource_relation.resource_id)
        # print(self.role_to_resources)

    def add_role_to_user(self, role_id, user_id):
        if user_id not in self.users:
            raise UnknownUser
        if role_id not in self.roles:
            raise UnknownRole
        self.user_to_roles[user_id].add(role_id)

    def remove_user_from_role(self, user_id, role_id):
        if user_id not in self.users:
            raise UnknownUser
        if role_id not in self.roles:
            raise UnknownRole
        if role_id not in self.user_to_roles[user_id]:
            raise UserNotAssignedToRole
        self.user_to_roles[user_id].remove(role_id)

    def get_roles_from_user(self, user_id):
        if user_id not in self.users:
            raise UnknownUser
        return self.user_to_roles[user_id]

    def get_resources_from_role_and_access_level(self, role_id, access_level):
        if role_id not in self.roles:
            return UnknownRole
        if access_level not in access_levels:
            return UnknownAccessLevel
        resources = set()
        if access_level == 'read':
            resources = resources.union(self.role_to_resources[role_id]['read'])
            resources = resources.union(self.role_to_resources[role_id]['write'])
            resources = resources.union(self.role_to_resources[role_id]['delete'])
        elif access_level == 'write':
            resources = resources.union(self.role_to_resources[role_id]['write'])
            resources = resources.union(self.role_to_resources[role_id]['delete'])
        elif access_level == 'delete':
            resources = resources.union(self.role_to_resources[role_id]['delete'])
        return resources
