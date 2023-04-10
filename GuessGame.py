import random
def generate_number(difficulty):
    secret_number=(random.randint(1, difficulty))
    return secret_number

def get_guess_from_user(difficulty):
    while True:
        try:
            guess_number = int(input(f"Please guess a number between 1 and {difficulty}: "))
            if guess_number < 1 or guess_number > difficulty:
                raise ValueError
            return guess_number
        except ValueError:
            print(f"Invalid input. Please enter a number between 1 and {difficulty}: ")

def compare_results(secret_number, guess_number):
    if guess_number == secret_number:
        return 0
    elif guess_number < secret_number:
        return -1
    else:
        return 1

def play():
    secret_number = generate_number()
    for i in range(5):
        guess_number = get_guess_from_user()
        if guess_number == secret_number:
            print("Congratulations, you won!")
            return True
        print("The secret number is", "greater" if guess_number < secret_number else "less", "than your guess.")
    print("Sorry, you lost the game.")
    return False