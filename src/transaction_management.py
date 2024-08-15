from datetime import datetime, timedelta

class TransactionManager:
    def __init__(self):
        self.transactions = {}  # Example transaction storage
        self.books = {}
        self.users = {}
        self.book_manager = None
        self.notification_system = None
        self.transaction_history = []

    def set_book_manager(self, book_manager):
        self.book_manager = book_manager

    def set_notification_system(self, notification_system):
        self.notification_system = notification_system

    def borrow_book(self, book_id, user_id):
        book = self.book_manager.get_book(book_id)
        if book and book['owner_id'] != user_id and book_id not in self.transactions:
            transaction_id = len(self.transactions) + 1
            self.transactions[transaction_id] = {
                'book_id': book_id,
                'borrower_id': user_id,
                'status': 'Borrowed'
            }
            self.notification_system.generate_transaction_notification(user_id, book['title'], 'borrowed')
            return transaction_id
        return None

    def return_book(self, transaction_id):
        if transaction_id in self.transactions and self.transactions[transaction_id]['status'] == 'Borrowed':
            self.transactions[transaction_id]['status'] = 'Returned'
            transaction = self.transactions[transaction_id]
            book = self.book_manager.get_book(transaction['book_id'])
            self.notification_system.generate_transaction_notification(transaction['borrower_id'], book['title'], 'returned')
            return True
        return False

    def get_user_transactions(self, user_id):
        return [trans for trans in self.transactions.values() if trans['borrower_id'] == user_id]
    
    def update_book_condition(self, book_id, condition):
        book = self.book_manager.get_book(book_id)
        print(f"Book before update: {book}")  # Debugging line
        if book:
            book['condition'] = condition
            print(f"Book after update: {book}")  # Debugging line
            return True
        print(f"Book with ID {book_id} not found.")
        return False
    
    def get_book_condition(self, book_id):
        book = self.book_manager.get_book(book_id)
        if book:
            return book.get('condition', 'Unknown')
        return 'Unknown'
    
    def filter_books_by_condition(self, condition):
        return [book for book in self.books.values() if book.condition == condition]
    
    def filter_books_by_availability(self, available):
        return [book for book in self.books.values() if book.available == available]
    
    def log_transaction(self, user_id, book_id, action):
        self.transaction_history.append({
            'user_id': user_id,
            'book_id': book_id,
            'action': action,
            'timestamp': datetime.now()
        })

    def get_transaction_history(self):
        return self.transaction_history

class Book:
    def __init__(self, id, title, available=True, condition='New'):
        self.id = id
        self.title = title
        self.available = available
        self.condition = condition
    
    def update_condition(self, new_condition):
        self.condition = new_condition