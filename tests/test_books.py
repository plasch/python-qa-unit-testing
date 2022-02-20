import unittest

from src import Book


class TestBookClass(unittest.TestCase):
    BOOK_DATA = {"title": "Просто Книга", "author": "Просто Автор",
                 "genre": "Боевик", "year": "2020"}

    def setUp(self):
        self.book = Book(self.BOOK_DATA)

    def test_book_attributes(self):
        self.assertEqual(self.book.title, self.BOOK_DATA["title"])
        self.assertEqual(self.book.genre, self.BOOK_DATA["genre"])
        self.assertEqual(self.book.year, self.BOOK_DATA["year"])
        self.assertEqual(self.book.author, self.BOOK_DATA["author"])

    def test_book_validation(self):
        self.assertRaises(ValueError, Book, {"title": "Название"})
        self.assertRaises(ValueError, Book, {"title": "Название", "author": "Some author"})
        self.assertRaises(ValueError, Book, {"title": "Просто Книга", "author": "Просто Автор", "genre": "Боевик"})

    def test_book_representation(self):
        self.assertEqual(str(self.book), f"Книга: {self.BOOK_DATA['title']}, Автор: {self.BOOK_DATA['author']}")
