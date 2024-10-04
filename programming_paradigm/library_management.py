class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def checked_out(self):
        return self._is_checked_out
    
    def change_check_status(self):
        self._is_checked_out = not self._is_checked_out


class Library:
    _books = []
    _borrowed = []

    def add_book(cls, book):
        cls._books.append(book)

    def check_out_book(cls, title):
        for book in cls._books:
            if book.title == title and not book.checked_out:
                cls._borrowed.append(book)
                book.change_check_status()
                Library._books.remove(book)
    
    def return_book(cls, title):
        for book in Library._borrowed:
            if book.title == title and book.checked_out:
                cls._books.append(book)
                cls._borrowed.remove(book)
    
    def list_available_books():
        for books in Library._books:
            print(books)

