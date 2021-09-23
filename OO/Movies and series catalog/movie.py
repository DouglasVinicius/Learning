from program import Program

class Movie(Program):
    def __init__(self, name, release_year, genre, duration_time):
        super().__init__(name, release_year, genre)
        self.__duration_time = duration_time

    @property
    def duration_time(self):
        return self.__duration_time