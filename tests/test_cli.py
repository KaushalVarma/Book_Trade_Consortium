# File: G:\E_drive_data\GitHubProjects\Book_Trade_Conssortium\tests\test_cli.py

import unittest
from unittest.mock import patch
from src.cli import BookTradeConsortiumCLI, TransactionManager

class TestBookTradeConsortiumCLI(unittest.TestCase):
    
    def setUp(self):
        self.transaction_manager = TransactionManager()
        self.transaction_manager.books = {
            '1': {'id': '1', 'title': 'Python Programming', 'available': True},
            '2': {'id': '2', 'title': 'Data Structures', 'available': True}
        }
        self.transaction_manager.users = {
            '101': {'id': '101', 'name': 'Alice', 'email': 'alice@example.com'},
            '102': {'id': '102', 'name': 'Bob', 'email': 'bob@example.com'}
        }
        self.cli = BookTradeConsortiumCLI(self.transaction_manager)

    @patch('builtins.input', side_effect=['1', '101'])
    def test_lend_a_book(self, mock_input):
        with patch('builtins.print') as mocked_print:
            self.cli.lend_a_book()
            mocked_print.assert_called_with("Book 'Python Programming' lent to user 'Alice'.")

    @patch('builtins.input', side_effect=['Python'])
    def test_find_a_book(self, mock_input):
        with patch('builtins.print') as mocked_print:
            self.cli.find_a_book()
            mocked_print.assert_any_call("ID: 1, Title: Python Programming, Available: True")

    @patch('builtins.input', side_effect=['101'])
    def test_view_profile(self, mock_input):
        with patch('builtins.print') as mocked_print:
            self.cli.view_profile()
            mocked_print.assert_called_with("User ID: 101, Name: Alice, Email: alice@example.com")

if __name__ == "__main__":
    unittest.main()
