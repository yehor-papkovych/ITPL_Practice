import Functions

if __name__ == '__main__':

    go = Functions.start()

    while go:
        movie = Functions.get_info()

        Functions.choose_movie(movie)

        go = Functions.go()

    print("Thank you! Goodbye!")
