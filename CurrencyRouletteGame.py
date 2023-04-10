import requests
import random

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_money_interval(self,total_value_of_money):
        url = 'https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=YOUR_API_KEY'
        response = requests.get(url)
        exchange_rate = response.json()['USD_ILS']
        lower_bound = total_value_of_money - (5 - self.difficulty) * exchange_rate
        upper_bound = total_value_of_money + (5 - self.difficulty) * exchange_rate
        return (lower_bound,upper_bound)

    def get_guess_from_user(self, total_value_of_money):
        guess = input(f'Guess the value of {total_value_of_money} USD in ILS: ')
        return float(guess)

    def play(self):
        total_value_of_money = random.randint(1, 100)
        interval = self.get_money_interval(total_value_of_money)
        guess = self.get_guess_from_user(total_value_of_money)
        if interval[0] <= guess <= interval[1]:
            print('Congratulations! You won!')
            return True
        else:
            print(f'Sorry, you lost. The value was {total_value_of_money} USD = {total_value_of_money * exchange_rate} ILS.')
            return False
