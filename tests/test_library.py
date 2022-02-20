import unittest

from src import Book
from src import BookShelf
from src import Library


class TestBookShelfClass(unittest.TestCase):
    BOOK1 = Book({"title": "Просто Книга", "author": "Просто Автор",
                  "genre": "Боевик", "year": "2020"})

    BOOK2 = Book({"title": "Фантастика1", "author": "Просто Автор",
                  "genre": "Фантастика", "year": "2000"})

    BOOK3 = Book({"title": "Фантастика2", "author": "Просто Автор",
                  "genre": "Фантастика", "year": "2020"})

    def setUp(self):
        self.library = Library("Test Library")

    def test_represent_library(self):
        self.assertEqual(str(self.library), "Test Library")

    def test_bookshelf_add_to_library(self):
        self.assertFalse(self.library.shelf_exists("Боевик"))
        self.library.add_bookshelf(BookShelf("Боевик"))
        self.assertTrue(self.library.shelf_exists("Боевик"))

    def test_library_has_book(self):
        self.library.add_book(self.BOOK3)
        self.assertTrue(self.library.shelf_exists(self.BOOK3.genre))
        self.assertTrue(self.library.has_book(self.BOOK3.title))

    def test_take_book_from_library(self):
        self.library.add_book(self.BOOK1)
        self.assertTrue(self.library.shelf_exists(self.BOOK1.genre))
        self.assertEqual(self.library.give_book(self.BOOK1.title), self.BOOK1)

    def test_take_not_existing_book(self):
        self.library.add_book(self.BOOK1)
        self.assertTrue(self.library.shelf_exists(self.BOOK1.genre))
        self.assertEqual(self.library.give_book(self.BOOK2.title), "Нет такой книги в библиотеке!")
