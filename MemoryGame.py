import random
import time
def generate_sequence(difficulty):
    return random.sample(range(1, 102), difficulty)

def get_list_from_user(difficulty):
    numbers = []
    for i in range(difficulty):
        number = int(input(f"Please enter number {i + 1} of {difficulty}: "))
        numbers.append(number)
    return numbers

def is_list_equal(list1,list2):
    return list1 == list2

def play(difficulty):
    seq = generate_sequence(difficulty)
    print(f"Remember these numbers:\n{seq}\n")
    user_list = get_list_from_user(difficulty)
    return is_list_equal(seq, user_list)
