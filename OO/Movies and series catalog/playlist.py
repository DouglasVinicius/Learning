from program import Program

class Playlist:
    def __init__(self, name):
        self.__name = name
        self.__programs = []

    @property
    def name(self):
        return self.__name.title()

    def show_one_program(self, index):
        print(index+1, '-', end=" ")
        self.__programs[index].print_prog()

    def show_playlist(self):
        print(f"Playlist '{self.__name.title()}':")
        for index, program in enumerate(self.__programs):
            print(index+1, '-', end=" ")
            program.print_prog()

    def playlist_len(self):
        return len(self.__programs)

    def add_program(self, program):
        print(f"You add {program.name}!")
        self.__programs.append(program)

    def add_playlist(self, playlist):
        for program in playlist:
            self.add_program(program)

    def remove_program(self, index_program):
        print(f"You remove {self.__programs[index_program].name}!")
        self.__programs.remove(index_program)

    def remove_playlist(self, index_list):
        for index_program in index_list:
            self.remove_program(index_program)

    def mv_program(self, index_one, index_two):
        print(f"You swap {self.__programs[index_one].name} and {self.__programs[index_two].name} in the queue!")
        self.__programs[index_one], self.__programs[index_two] = self.__programs[index_two], self.__programs[index_one]

    def like_program(self, index_program):
        print(f"You like {self.__programs[index_program].name}!")
        self.__programs[index_program].give_like()
    
    def like_playlist(self):
        for index in range(0, len(self.__programs)):
            self.like_program(index)