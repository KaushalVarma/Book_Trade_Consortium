class BookManager:
    def __init__(self):
        self.books = {}  # Example book storage

    def add_book(self, title, author, condition, owner_id):
        book_id = len(self.books) + 1
        self.books[book_id] = {
            'title': title,
            'author': author,
            'condition': condition,
            'owner_id': owner_id
        }
        return book_id

    def get_book(self, book_id):
        return self.books.get(book_id, None)

    def update_book(self, book_id, title=None, author=None, condition=None):
        if book_id in self.books:
            if title:
                self.books[book_id]['title'] = title
            if author:
                self.books[book_id]['author'] = author
            if condition:
                self.books[book_id]['condition'] = condition
            return True
        return False

    def delete_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False
