import unittest

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AuthenticationService:
    def __init__(self):
        self.users = []

    def register_user(self, username, password):
        user = User(username, password)
        self.users.append(user)

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False

class AuthenticationTest(unittest.TestCase):
    def setUp(self):
        # Se ejecuta antes de cada prueba
        self.auth_service = AuthenticationService()
        self.auth_service.register_user('usuario1', 'contraseña123')
        self.auth_service.register_user('usuario2', 'abcde')

    def test_login_successful(self):
        result = self.auth_service.login('usuario1', 'contraseña123')
        self.assertTrue(result)

    def test_login_failure_wrong_password(self):
        result = self.auth_service.login('usuario1', 'incorrecta')
        self.assertFalse(result)

    def test_login_failure_unknown_user(self):
        result = self.auth_service.login('usuario3', 'contraseña123')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()






