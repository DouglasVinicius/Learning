from program import Program

class Serie(Program):
    def __init__(self, name, release_year, genre, seasons):
        super().__init__(name, release_year, genre)
        self.__seasons = seasons

    @property
    def seasons(self):
        return self.__seasons

    def __str__(self):
        return f"Name: {self._name}, Realease Year: {self._release_year}, Genre: {self._genre}, Seasons: {self.__seasons}, Current likes: {self._likes}"
