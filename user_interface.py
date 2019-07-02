class UserInterface:
    def __init__(self, authorization):
        self.authorization = authorization

    def start(self):
        while True:
            try:
                line = input()
                tokens = line.split()
                if len(tokens) == 0:
                    command = 'help'
                else:
                    command = tokens[0]
                if command == 'help':
                    self.print_help()
                elif command == 'users':
                    self.print_all_users()
                elif command == 'roles':
                    self.print_all_roles()
                elif command == 'resources':
                    self.print_all_resources()
                elif command == 'authorize':
                    self.authorize(tokens[1:])
                elif command == 'assign':
                    self.assign(tokens[1:])
                elif command == 'remove':
                    self.remove(tokens[1:])
                elif command == 'exit':
                    return
                else:
                    self.print_unknown_command()
            except Exception as e:
                print('Error: {}'.format(e.__class__.__name__))

    def print_help(self):
        print(
            'Role Based Access Control System\n'
            'Commands:\n'
            '\t1. help: To know about available commands.\n'
            '\t2. users: To see all users.\n'
            '\t3. roles: To see all roles.\n'
            '\t4. resources: To see all resources.\n'
            '\t5. assign <user_id> <role_id>: To assign a user to a role.\n'
            '\t6. remove <user_id> <role_id>: To remove a user from a role.\n'
            '\t7. exit: To exit from command prompt.'
        )

    def print_unknown_command(self):
        print(
            "Unknown command. Use 'help' to see available commands."
        )


    def print_entities(self, entities):
        for entity in entities.values():
            print(str(entity))

    def print_all_users(self):
        users = self.authorization.get_all_users()
        print('All users:')
        self.print_entities(users)

    def print_all_resources(self):
        resources = self.authorization.get_all_resources()
        print('All resources:')
        self.print_entities(resources)

    def print_all_roles(self):
        roles = self.authorization.get_all_roles()
        print('All roles:')
        self.print_entities(roles)

    def authorize(self, args):
        user_id = args[0]
        resource_id = args[1]
        action = args[2]
        if self.authorization.is_authorized(user_id, resource_id, action):
            print('YES')
        else:
            print('NO')

    def assign(self, args):
        user_id = args[0]
        role_id = args[1]
        self.authorization.add_role_to_user(role_id, user_id)

    def remove(self, args):
        user_id = args[0]
        role_id = args[1]
        self.authorization.remove_user_from_role(user_id, role_id)
