class TransactionManager:
    def __init__(self):
        self.books = {}  # Example data structure to store book info
        self.users = {}  # Example data structure to store user info
        self.transactions = []  # Example data structure to store transactions

    def lend_book(self, book_id, user_id):
        if book_id in self.books and user_id in self.users:
            book = self.books[book_id]
            user = self.users[user_id]
            if book['available']:
                book['available'] = False
                self.transactions.append({'book_id': book_id, 'user_id': user_id, 'type': 'lend'})
                return f"Book '{book['title']}' lent to user '{user['name']}'."
            else:
                return f"Book '{book['title']}' is currently unavailable."
        else:
            return "Invalid book ID or user ID."

    def find_books(self, query):
        matching_books = [book for book in self.books.values() if query.lower() in book['title'].lower()]
        return matching_books

    def get_user_profile(self, user_id):
        if user_id in self.users:
            user = self.users[user_id]
            return user
        else:
            return None


class BookTradeConsortiumCLI:
    def __init__(self, transaction_manager):
        self.transaction_manager = transaction_manager

    def main_menu(self):
        while True:
            print("\nWelcome to the Book Trade Consortium")
            print("1. Lend a Book")
            print("2. Find a Book")
            print("3. View Profile")
            print("4. Exit")
            choice = input("Please select an option (1-4): ")

            if choice == '1':
                self.lend_a_book()
            elif choice == '2':
                self.find_a_book()
            elif choice == '3':
                self.view_profile()
            elif choice == '4':
                print("Thank you for using the Book Trade Consortium. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def lend_a_book(self):
        book_id = input("Enter the ID of the book to lend: ")
        user_id = input("Enter the ID of the user: ")
        result = self.transaction_manager.lend_book(book_id, user_id)
        print(result)

    def find_a_book(self):
        query = input("Enter the title or part of the title to search: ")
        matching_books = self.transaction_manager.find_books(query)
        if matching_books:
            print("Matching books:")
            for book in matching_books:
                print(f"ID: {book['id']}, Title: {book['title']}, Available: {book['available']}")
        else:
            print("No matching books found.")

    def view_profile(self):
        user_id = input("Enter the ID of the user: ")
        user = self.transaction_manager.get_user_profile(user_id)
        if user:
            print(f"User ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
        else:
            print("User not found.")

    def update_book_condition(self):
        book_id = input("Enter book ID: ")
        new_condition = input("Enter new condition: ")
        if self.transaction_manager.update_book_condition(book_id, new_condition):
            print(f"Condition of book ID {book_id} updated to '{new_condition}'.")
        else:
            print("Book not found.")

    def view_book_condition(self):
        book_id = input("Enter book ID: ")
        condition = self.transaction_manager.get_book_condition(book_id)
        if condition:
            print(f"Condition of book ID {book_id} is '{condition}'.")
        else:
            print("Book not found.")

    def find_books_by_condition(self):
        condition = input("Enter condition to search for: ")
        books = self.transaction_manager.filter_books_by_condition(condition)
        for book in books:
            print(f"ID: {book.id}, Title: {book.title}, Condition: {book.condition}")
    
    def find_books_by_availability(self):
        available = input("Enter availability (True/False): ").strip().capitalize() == 'True'
        books = self.transaction_manager.filter_books_by_availability(available)
        for book in books:
            print(f"ID: {book.id}, Title: {book.title}, Available: {book.available}")

    def view_transaction_history(self):
        history = self.transaction_manager.get_transaction_history()
        for entry in history:
            print(f"User ID: {entry['user_id']}, Book ID: {entry['book_id']}, Action: {entry['action']}, Time: {entry['timestamp']}")