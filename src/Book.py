# coding=utf-8
class Book:

    def __init__(self, data):
        if len(set(data.keys()).intersection({'title', 'author', 'year', 'genre'})) != 4:
            raise ValueError("Неправильный формат книги", data.keys())
        self._title = data.get('title')
        self._author = data.get('author')
        self._year = data.get('year')
        self._genre = data.get('genre')

    def __str__(self):
        return "Книга: {}, Автор: {}".format(self._title, self._author)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    @property
    def genre(self):
        return self._genre
