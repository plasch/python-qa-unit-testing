from .Book import Book


class BookShelf:

    def __init__(self, genre):
        self._genre = genre
        self._books = []

    def __str__(self):
        return self._genre

    @property
    def genre(self):
        return self._genre

    def put_book(self, book: Book):
        if not isinstance(book, Book):
            raise ValueError("Bookshelf can hold only books!")
        self._books.append(book)

    def take_book(self, title):
        book_index = self.has_book(title)
        if book_index is not None:
            return self._books.pop(book_index)

    @property
    def book_titles(self):
        return [book.title for book in self._books]

    @property
    def books_amount(self):
        return len(self._books)

    def has_book(self, title):
        try:
            return self.book_titles.index(title)
        except ValueError:
            return None
