import random


def get_guess(min_number, max_number):
    while True:
        try:
            guess = int(input(f"Guess a random number from {min_number} to {max_number}: "))
            if min_number <= guess <= max_number:
                return guess

            print(f"Please enter a number between {min_number} and {max_number}.")
        except ValueError:
            print(f"Please enter a valid number.")

