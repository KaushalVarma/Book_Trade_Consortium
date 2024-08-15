import datetime

class NotificationSystem:
    def __init__(self):
        self.notifications = {}

    def add_notification(self, user_id, message):
        notification_id = len(self.notifications) + 1
        self.notifications[notification_id] = {
            'user_id': user_id,
            'message': message,
            'timestamp': datetime.datetime.now()
        }
        return notification_id

    def get_user_notifications(self, user_id):
        return [notif for notif in self.notifications.values() if notif['user_id'] == user_id]

    def generate_reminder(self, user_id, book_title, days_before_due):
        message = f"Reminder: The book '{book_title}' is due in {days_before_due} days."
        self.add_notification(user_id, message)

    def generate_transaction_notification(self, user_id, book_title, transaction_type):
        message = f"Notification: You have {transaction_type} the book '{book_title}'."
        self.add_notification(user_id, message)
