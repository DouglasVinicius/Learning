from serie import Serie
from movie import Movie

def main():
    bla_serie = Serie("blabla bla", 1920, ['Ação', 'Aventura'], 3)
    print(f"Name: {bla_serie.name}", f"Year: {bla_serie.release_year}", f"Seasons: {bla_serie.seasons}", sep="\n")

if __name__ == "__main__":
    main()