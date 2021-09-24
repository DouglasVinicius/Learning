from abc import ABCMeta, abstractmethod

class Program(metaclass = ABCMeta):
    def __init__(self, name, release_year, genre):
        self._name = name
        self._release_year = release_year
        self._genre = genre
        self._likes = 0

    @property
    def name(self):
        return self._name.title()

    @property
    def release_year(self):
        return self._release_year

    @property
    def duration_time(self):
        return self._duration_time

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        self._genre = genre

    def give_like(self):
        self._likes += 1

    @abstractmethod
    def __str__(self):
        return f"Name: {self._name}, Realease Year: {self._release_year}, Genre: {self._genre}, Current likes: {self._likes}"
