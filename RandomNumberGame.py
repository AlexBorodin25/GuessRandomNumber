import random

def get_difficulty():
    while True:
        print("Choose difficulty:")
        print("1. Easy (1-10)")
        print("2. Medium (1-100)")
        print("3. Hard 1-1000)")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            return 1, 10
        elif choice == "2":
            return 1, 100
        elif choice == "3":
            return 1, 1000
        else:
            print("Please enter a valid choice.")

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
    min_number, max_number = get_difficulty()
    unknown_number = random.randint(min_number, max_number)
    guesses = 0

    print("The random number is generated. Try to guess it!")

    while True:
        guess = get_guess(min_number, max_number)
        guesses += 1

        if guess < unknown_number:
            print("Higher!")
        elif guess > unknown_number:
            print("Lower!")
        else:
            print("Correct!")
            print("It took you {guesses} guesses.".format(guesses=guesses))
            break

def main():
    while True:
        play_game()

        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()

        if play_again != "y":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()