# coding=utf-8
from src import BookShelf
from src import Book


class Library:

    def __init__(self, name):
        self.name = name
        self._bookshelves = []
        self._given_books = []

    def __str__(self):
        return self.name

    def _verify_book_data(self, data: dict):
        try:
            assert data.get("title")
            assert data.get("genre")
            assert data.get("year")
            assert data.get("author")
        except AssertionError:
            raise ValueError("У книги не хватает атрибутов для размещения в библиотеке")

    def shelf_exists(self, genre):
        return genre in self.bookshelves

    def has_book(self, title):
        for shelf in self._bookshelves:
            if shelf.has_book(title) is not None:
                return shelf.take_book(title)

    def add_book(self, book: [Book, dict]):
        if not isinstance(book, Book):
            self._verify_book_data(book)

        if not self.shelf_exists(book.genre):
            new_shelf = BookShelf(genre=book.genre)
            new_shelf.put_book(book)
            self.add_bookshelf(new_shelf)
        else:
            self.get_bookshelf(book.genre).put_book(book)

    def get_bookshelf(self, genre):
        if self.shelf_exists(genre):
            for shelf in self._bookshelves:
                if shelf.genre == genre:
                    return shelf

    def add_bookshelf(self, shelf: BookShelf):
        if not isinstance(shelf, BookShelf):
            raise ValueError("В библиотеку можно добавить только объекты класса BookShelf")
        self._bookshelves.append(shelf)

    @property
    def books_amount(self):
        return sum([shelf.books_amount for shelf in self._bookshelves])

    @property
    def bookshelves(self):
        return [bookshelf.genre for bookshelf in self._bookshelves]

    def give_book(self, title):
        book = self.has_book(title)
        return book if book is not None else "Нет такой книги в библиотеке!"

    def get_book_back(self, book: Book):
        self.add_book(book)
