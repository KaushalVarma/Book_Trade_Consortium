from user_management import UserManager
from book_management import BookManager
from transaction_management import TransactionManager
from notifications import NotificationSystem
from search_filter import SearchFilter

def main():
    user_manager = UserManager()
    book_manager = BookManager()
    transaction_manager = TransactionManager()
    notification_system = NotificationSystem()
    search_filter = SearchFilter()

    # Example usage
    user_id = user_manager.register_user("Alice", "alice@example.com", "password123")
    book_id = book_manager.add_book("The Great Gatsby", "F. Scott Fitzgerald", "New", user_id)
    search_results = search_filter.search_books("Gatsby")
    
    print(search_results)
    # More operations...

if __name__ == "__main__":
    main()
