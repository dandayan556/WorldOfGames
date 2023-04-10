import MemoryGame
import GuessGame
import CurrencyRouletteGame

def load_game():
    print("Please choose a game to play:")
    print("1.GuessGame")
    print("2.MemoryGame")
    print("3.CurrencyRouletteGame")
    game=int(input("Please enter game number"))
    difficulty=int(input("please choose difficulty level (1-3)"))

    if game==1:
        game=MemoryGame(difficulty)
        game.play()
    elif game==2:
        game=GuessGame(difficulty)
        game.play()
    elif game==3:
        game=CurrencyRouletteGame(difficulty)
        game.play()
    else:
         print("Invaild choise, please enter a number between (1-3)")

