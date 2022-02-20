# coding=utf-8
from src import Book
from src import Library

leninka = Library("Библиотека им. В.И. Ленина")

book1 = Book({"title": "Пикник на обочине", "author": "Братья Стругацкие",
              "genre": "Фантастика", "year": "1972"})

book2 = Book({"title": "История Российского государства", "author": "Борис Акунин",
              "genre": "История", "year": "2013"})

book3 = Book({"title": "Лучшая Книга", "author": "Лучший Автор",
              "genre": "Боевик", "year": "2020"})

book4 = Book({"title": "Просто Книга", "author": "Просто Автор",
              "genre": "Боевик", "year": "2020"})

leninka.add_book(book1)
leninka.add_book(book2)
leninka.add_book(book3)
leninka.add_book(book4)

print(leninka)
print(leninka.books_amount)
print(leninka.bookshelves)
print(leninka.give_book("Просто Книга"))
print(leninka.books_amount)
