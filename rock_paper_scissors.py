# Rock Paper Scissors
# Play against the computer and try to win the match!

import random


def get_choices():
    """Return valid choices for the game."""
    return ["rock", "paper", "scissors"]


def get_winner(player_choice, computer_choice):
    """Return the winner text for a round."""
    if player_choice == computer_choice:
        return "draw"

    winning_combinations = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    if winning_combinations[player_choice] == computer_choice:
        return "player"
    return "computer"


def display_choices(player_choice, computer_choice):
    """Display the selected options for the round."""
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")


def play_round(player_score, computer_score):
    """Play one round and return updated scores."""
    choices = get_choices()
    print("\nChoose: rock, paper, or scissors")
    player_choice = input("Your move: ").strip().lower()

    if player_choice not in choices:
        print("Invalid choice! Please type rock, paper, or scissors.")
        return player_score, computer_score

    computer_choice = random.choice(choices)
    display_choices(player_choice, computer_choice)

    result = get_winner(player_choice, computer_choice)

    if result == "draw":
        print("It's a draw! No points awarded.")
    elif result == "player":
        player_score += 1
        print("You win this round!")
    else:
        computer_score += 1
        print("Computer wins this round!")

    return player_score, computer_score


def play_game():
    """Main game loop for Rock Paper Scissors."""
    player_score = 0
    computer_score = 0
    rounds = 0

    print("\n=== Welcome to Rock Paper Scissors ===")
    print("First to win 5 rounds wins the match!")

    while player_score < 5 and computer_score < 5:
        player_score, computer_score = play_round(player_score, computer_score)
        rounds += 1

        print(f"\nScore: You {player_score} - {computer_score} Computer")

        if player_score >= 5 or computer_score >= 5:
            break

        again = input("Play another round? (y/n): ").strip().lower()
        while again not in ["y", "n"]:
            print("Please enter 'y' or 'n'.")
            again = input("Play another round? (y/n): ").strip().lower()

        if again == "n":
            print("Thanks for playing!")
            return

    if player_score > computer_score:
        print("\n🎉 You won the match!")
    elif computer_score > player_score:
        print("\n💻 Computer won the match!")
    else:
        print("\nIt's a draw!")

    print(f"Final score: You {player_score} - {computer_score} Computer")


def main():
    """Menu loop for the game."""
    print("=== Rock Paper Scissors ===")

    while True:
        print("\nOptions:")
        print("1. Play")
        print("2. Exit")

        choice = input("\nEnter choice (1/2): ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1 or 2.")


if __name__ == "__main__":
    main()
