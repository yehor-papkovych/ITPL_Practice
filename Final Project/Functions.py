class Movie:
    def __init__(self, name, genre, length, animation):
        self.name = name
        self.genre = genre
        self.length = length
        self.animation = animation

def start():
    word = input("Do you want to start? Type 'y' if yes, type 'n' or anything else if no.\n")
    if word == 'y' or word == 'Y':
        return True
    return False

def go():
    word = input("Do you want to continue? Type 'y' if yes, type 'n' if no.\n")
    if word == 'y' or word == 'Y':
        return True
    return False

def get_info():
    name = input("Hello! What is your name?\n")
    print("What is your favorite movie genre, " + name + "?")

    genres = ['drama', 'horror', 'action', 'romance', 'comedy', 'thriller']
    genre = input("Type in one of the options: 'romance', 'action', 'drama', 'horror', 'comedy', 'thriller'.\n")
    while genre not in genres:
        print('There is no such genre! Try again!')
        genre = input("Type in one of the options: 'romance', 'action', 'drama', 'horror', 'comedy', 'thriller'.\n")

    length = input("Do you prefer movies or TV series? Type in: 'movies' or 'series'.\n")
    while length not in ['movies', 'series']:
        print('There is no such option. Try again!')
        length = input("Do you prefer movies or TV series? Type in: 'movies' or 'series'.\n")

    animation = input("Do you like animated movies? Type in: 'yes' or 'no'.\n")
    while animation not in ['yes', 'no']:
        print('There is no such option. Try again!')
        animation = input("Do you like animated movies? Type in: 'yes' or 'no'.\n")

    return Movie(name, genre, length, animation)

def print_preferences(value):
    print("You might like: " + "'" + value + "'")

def choose_animation(movie, movies):
    if movie.animation == 'yes':
        print_preferences(movies[0])
    elif movie.animation == 'no':
        print_preferences(movies[1])

def choose_length(movie, movies):
    if movie.length == 'movies':
        choose_animation(movie, movies[:2])
    elif movie.length == 'series':
        choose_animation(movie, movies[2:])

def choose_movie(movie):
    dramas = ["Violet Evergarden", "Forrest Gump", "Cyberpunk Edgerunners", "Breaking Bad"]
    horrors = ["The Island of Giant Insects", "It", "Japanese Tales of Massacre", "Walking Dead"]
    actions = ["Invincible", "Mission Impossible", "Vinland Saga", "Narcos"]
    romances = ["Suzume", "Titanic", "Kaguya-Sama: Love is War", "Emily in Paris"]
    comedies = ["Shrek", "Men in Black", "Rick and Morty", "Sex Education"]
    thrillers = ["Batman: Year One", "Black Swan", "Heavenly Delusion", "Black Mirror"]

    if movie.genre == 'drama':
        choose_length(movie, dramas)
    elif movie.genre == 'horror':
        choose_length(movie, horrors)
    elif movie.genre == 'action':
        choose_length(movie, actions)
    elif movie.genre == 'romance':
        choose_length(movie, romances)
    elif movie.genre == 'comedy':
        choose_length(movie, comedies)
    elif movie.genre == 'thriller':
        choose_length(movie, thrillers)