import unittest

from src import Book
from src import BookShelf


class TestBookShelfClass(unittest.TestCase):

    BOOK1 = Book({"title": "Просто Книга", "author": "Просто Автор",
                 "genre": "Боевик", "year": "2020"})

    BOOK2 = Book({"title": "Фантастика1", "author": "Просто Автор",
                 "genre": "Фантастика", "year": "2000"})

    BOOK3 = Book({"title": "Фантастика2", "author": "Просто Автор",
                 "genre": "Фантастика", "year": "2020"})

    def setUp(self):
        self.bookshelf = BookShelf("Фантастика")
        self.bookshelf.put_book(self.BOOK1)
        self.bookshelf.put_book(self.BOOK2)
        self.bookshelf.put_book(self.BOOK3)

    def test_books_on_bookshelf(self):
        self.assertEqual(self.bookshelf.books_amount, 3)

    def test_take_book_from_shelf(self):
        self.bookshelf.take_book(self.BOOK3.title)
        self.assertEqual(self.bookshelf.books_amount, 2)

    def test_take_all_books_from_shelf(self):
        self.bookshelf.take_book(self.BOOK1.title)
        self.bookshelf.take_book(self.BOOK2.title)
        self.assertEqual(self.bookshelf.books_amount, 1)
