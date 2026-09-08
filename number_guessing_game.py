# Number Guessing Game
# Try to guess the hidden number before you run out of attempts.

import random


def play_round():
    """Play one round of the number guessing game."""
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("\n=== Guess the Number ===")
    print(f"I picked a number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return True

        if guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Attempts left: {remaining}")

    print(f"Sorry, you ran out of attempts. The number was {secret_number}.")
    return False


def main():
    """Main menu for the game."""
    print("=== Number Guessing Game ===")

    while True:
        print("\nOptions:")
        print("1. Play")
        print("2. Exit")

        choice = input("\nEnter choice (1/2): ")

        if choice == "1":
            play_round()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1 or 2.")


if __name__ == "__main__":
    main()
