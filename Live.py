def welcome(name):
    return f"Hello {name} and welcome to the World of Games.Here you can find many cool games to play."


def load_game():
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("3. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    game=input("Please choose a game to play:")
    difficulty = input("Please enter difficulty level from 1 to 5: ")

    while game not in ["1", "2", "3"]:
        game = input("Invalid")
    while difficulty not in ["1", "2", "3", "4", "5"]:
        difficulty = input("Invalid")
    return game,difficulty
