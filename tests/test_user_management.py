import unittest
from src.user_management import UserManager

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager()

    def test_register_user(self):
        user_id = self.user_manager.register_user("Alice", "alice@example.com", "password123")
        user = self.user_manager.get_user(user_id)
        self.assertEqual(user['name'], "Alice")
        self.assertEqual(user['email'], "alice@example.com")

    def test_login_user(self):
        user_id = self.user_manager.register_user("Bob", "bob@example.com", "securepass")
        logged_in_user_id = self.user_manager.login_user("bob@example.com", "securepass")
        self.assertEqual(logged_in_user_id, user_id)
        self.assertIsNone(self.user_manager.login_user("bob@example.com", "wrongpass"))

    def test_reset_password(self):
        user_id = self.user_manager.register_user("Carol", "carol@example.com", "oldpass")
        self.assertTrue(self.user_manager.reset_password(user_id, "newpass"))
        self.assertIsNone(self.user_manager.login_user("carol@example.com", "oldpass"))
        logged_in_user_id = self.user_manager.login_user("carol@example.com", "newpass")
        self.assertEqual(logged_in_user_id, user_id)

if __name__ == "__main__":
    unittest.main()
