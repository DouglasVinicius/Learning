from serie import Serie
from movie import Movie
from playlist import Playlist

def create_playlist(playlists):
    name = input("Name: ")
    playlists.append(Playlist(name))
    print("You created a playlist with success!")

def show_current_playlists(playlists):
    print("CURRENT PLAYLISTS:", end="\n\n")
    for index_playlist, playlist in enumerate(playlists):
        print(index_playlist+1, '-', end=' ')
        print(f"Playlist: {playlist.name}, size: {len(playlist)}:")
        for index_programs, program in enumerate(playlist):
            print(index_programs+1, '-', end=" ")
            print(program)
        print()

def add_new_program(playlists):
    try:
        playlist_index = int(input("Which playlist do you want add the program (index)? "))-1
        choice = int(input("1 - Movie     2 - Serie: "))

        if(choice == 1):
            name = input("New program name: ")
            release_year = input("New program release year: ")
            genre = input("New program genre: ")
            duration_time = input("New program duration: ")

            playlists[playlist_index].add_program(Movie(name, release_year, genre, duration_time))
        elif(choice == 2):
            name = input("New program name: ")
            release_year = input("New program release year: ")
            genre = input("New program genre: ")
            seasons = input("New program seasons: ")

            playlists[playlist_index].add_program(Serie(name, release_year, genre, seasons))
        else:
            print("Invalid value!")
    except:
        print("Invalid value!")

def give_likes(playlists):
    try:
        playlist_index = int(input("Which playlist do you want like (index)? "))-1
        program_index = int(input("Index of a program or 0 for like all the programs in playlist: "))-1

        all = (program_index == 0)
        if(all):
            playlists[playlist_index].like_program(program_index)
        else:
            playlists[playlist_index].like_playlist()
    except:
        print("Invalid value!")

def swap_queue(playlists):
    try:
        playlist_index = int(input("Which playlist do you want swap programs (index)? "))-1
        program_index_one = int(input("Index of a first program that you want swap: "))-1
        program_index_two = int(input("Index of a second program that you want swap: "))-1

        playlists[playlist_index].mv_program(program_index_one, program_index_two)
    except:
        print("Invalid value!")

def main():
    continuar = True
    playlists = []

    while(continuar):
        try:
            choice = int(input("1 - Create a new playlist     2 - Add a new program to a playlist     3 - Give likes     4 - Swap queue     5 - Show playlists     0 - Exit: "))
            exit = (choice == 0)

            if(not exit):
                if(choice == 1):
                    create_playlist(playlists)
                elif(choice == 2):
                    add_new_program(playlists)
                elif(choice == 3):
                    give_likes(playlists)
                elif(choice == 4):
                    swap_queue(playlists)
                elif(choice == 5):
                    show_current_playlists(playlists)
                else:
                    print("Invalid value!")
            else:
                break
        except:
            print("Invalid value!")

    print("Thank you!")

if __name__ == "__main__":
    main()