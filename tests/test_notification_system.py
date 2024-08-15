import unittest
from src.notification_system import NotificationSystem

class TestNotificationSystem(unittest.TestCase):
    def setUp(self):
        self.notification_system = NotificationSystem()

    def test_add_notification(self):
        notification_id = self.notification_system.add_notification(1, "Test Notification")
        notification = self.notification_system.notifications[notification_id]
        self.assertEqual(notification['user_id'], 1)
        self.assertEqual(notification['message'], "Test Notification")

    def test_get_user_notifications(self):
        self.notification_system.add_notification(1, "Test Notification 1")
        self.notification_system.add_notification(2, "Test Notification 2")
        user_notifications = self.notification_system.get_user_notifications(1)
        self.assertEqual(len(user_notifications), 1)
        self.assertEqual(user_notifications[0]['user_id'], 1)

    def test_generate_reminder(self):
        self.notification_system.generate_reminder(1, "1984", 2)
        notifications = self.notification_system.get_user_notifications(1)
        self.assertTrue(any("due in 2 days" in notif['message'] for notif in notifications))

    def test_generate_transaction_notification(self):
        self.notification_system.generate_transaction_notification(1, "1984", "borrowed")
        notifications = self.notification_system.get_user_notifications(1)
        self.assertTrue(any("borrowed the book '1984'" in notif['message'] for notif in notifications))

if __name__ == "__main__":
    unittest.main()
