from program import Program

class Serie(Program):
    def __init__(self, name, release_year, genre, seasons):
        super().__init__(name, release_year, genre)
        self.__seasons = seasons

    @property
    def seasons(self):
        return self.__seasons
