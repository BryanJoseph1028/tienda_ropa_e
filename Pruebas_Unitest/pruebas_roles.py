import unittest

class User:
    def __init__(self, username, roles=None):
        self.username = username
        self.roles = roles if roles is not None else []

    def add_role(self, role):
        self.roles.append(role)

    def remove_role(self, role):
        self.roles.remove(role)

class RoleManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def assign_role(self, user, role):
        user.add_role(role)

    def remove_role(self, user, role):
        user.remove_role(role)

class RoleManagerTest(unittest.TestCase):
    def setUp(self):
        # Se ejecuta antes de cada prueba
        self.role_manager = RoleManager()
        self.user1 = User('usuario1')
        self.user2 = User('usuario2')

    def test_assign_role(self):
        self.role_manager.add_user(self.user1)
        self.role_manager.assign_role(self.user1, 'cliente')
        self.assertIn('cliente', self.user1.roles)

    def test_remove_role(self):
        self.role_manager.add_user(self.user2)
        self.role_manager.assign_role(self.user2, 'admin')
        self.role_manager.remove_role(self.user2, 'admin')
        self.assertNotIn('admin', self.user2.roles)

if __name__ == '__main__':
    unittest.main()





