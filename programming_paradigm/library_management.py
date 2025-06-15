class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
        
    def return_book(self):
        """Mark the book as returned"""
        if not self.is_checked_out:
            return False  # Wasn't checked out
        self.is_checked_out = False
        return True


class Library:
    def __init__(self):
        self._books = []

    
    def add_book(self, book):
        if not book:
            raise ValueError("Can only add Book objects to thr library")
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower and not book._is_checked_out:
                book._is_checked_out = True
                return
    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and book._is_checked_out:
                book._is_checked_out = False
                return
            
    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if not available_books:
            print("No books currently available")
            return
        
    

        