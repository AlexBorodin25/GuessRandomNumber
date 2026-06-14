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

def play_game():
    unknown_number = random.randint(min_number, max_number)
    guesses = 0

    print("\n The random number is generated. Try to guess it!")

    while True:
        guess = get_guess(min_number, max_number)
        guesses += 1

        if guess < unknown_number:
            print("Higher!")
        elif guess > unknown_number:
            print("Lower!")
        else:
            print("Correct!")
            print("It took you {guesses} guesses.")
            break

def main():
    while True:
        play_game()

        play_again = input("\nWould you like to play again? (y/n): ")
        if play_again == "y":
            play_game()
        else:
            print("Thank you for playing!")

if __name__ == "__main__":
    main()