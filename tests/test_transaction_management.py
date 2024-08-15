import unittest
from src.transaction_management import TransactionManager
from src.book_management import BookManager
from src.notification_system import NotificationSystem

class TestTransactionManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()
        self.transaction_manager = TransactionManager()
        self.transaction_manager.set_book_manager(self.book_manager)

        self.notification_system = NotificationSystem()
        self.transaction_manager.set_notification_system(self.notification_system)

        # Ensure book ID matches the one used in the test
        self.book_id = self.book_manager.add_book("Animal Farm", "George Orwell", "Good", "1")  

    def test_borrow_book(self):
        transaction_id = self.transaction_manager.borrow_book(self.book_id, 2)
        transaction = self.transaction_manager.transactions[transaction_id]
        self.assertEqual(transaction['book_id'], self.book_id)
        self.assertEqual(transaction['borrower_id'], 2)
        self.assertEqual(transaction['status'], 'Borrowed')

    def test_return_book(self):
        transaction_id = self.transaction_manager.borrow_book(self.book_id, 2)
        self.assertTrue(self.transaction_manager.return_book(transaction_id))
        transaction = self.transaction_manager.transactions[transaction_id]
        self.assertEqual(transaction['status'], 'Returned')

    def test_get_user_transactions(self):
        transaction_id1 = self.transaction_manager.borrow_book(self.book_id, 2)
        transaction_id2 = self.transaction_manager.borrow_book(self.book_id, 3)
        transactions = self.transaction_manager.get_user_transactions(2)
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]['borrower_id'], 2)

    def test_update_book_condition(self):
        result = self.transaction_manager.update_book_condition(1, "Used")  
        self.assertTrue(result)
        self.assertEqual(self.book_manager.get_book(1)['condition'], "Used")

if __name__ == "__main__":
    unittest.main()
