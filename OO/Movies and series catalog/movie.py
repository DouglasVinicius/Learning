from program import Program

class Movie(Program):
    def __init__(self, name, release_year, genre, duration_time):
        super().__init__(name, release_year, genre)
        self.__duration_time = duration_time

    @property
    def duration_time(self):
        return self.__duration_time

    def print_prog(self):
        print(f"Name: {self._name}, Realease Year: {self._release_year}, Genre: {self._genre}, Duration: {self.__duration_time}min, Current likes: {self._likes}")