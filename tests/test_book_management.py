import unittest
from src.book_management import BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()

    def test_add_book(self):
        book_id = self.book_manager.add_book("1984", "George Orwell", "New", 1)
        book = self.book_manager.get_book(book_id)
        self.assertEqual(book['title'], "1984")
        self.assertEqual(book['author'], "George Orwell")
        self.assertEqual(book['condition'], "New")

    def test_update_book(self):
        book_id = self.book_manager.add_book("To Kill a Mockingbird", "Harper Lee", "Good", 2)
        self.book_manager.update_book(book_id, title="To Kill a Mockingbird - Updated", condition="Like New")
        book = self.book_manager.get_book(book_id)
        self.assertEqual(book['title'], "To Kill a Mockingbird - Updated")
        self.assertEqual(book['condition'], "Like New")

    def test_delete_book(self):
        book_id = self.book_manager.add_book("The Catcher in the Rye", "J.D. Salinger", "Fair", 3)
        self.assertTrue(self.book_manager.delete_book(book_id))
        self.assertIsNone(self.book_manager.get_book(book_id))

if __name__ == "__main__":
    unittest.main()
