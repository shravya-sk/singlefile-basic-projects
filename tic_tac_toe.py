# Tic-Tac-Toe Game
# Play a classic two-player game in the terminal

def display_board(board):
    """Display the current board"""
    print(f"\n {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}\n")


def check_winner(board, player):
    """Return True when the player has three matching spaces"""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(all(board[position] == player for position in combination)
               for combination in winning_combinations)


def get_move(board, player):
    """Get and validate a move from the current player"""
    while True:
        move = input(f"Player {player}, choose a space (1-9): ")

        if not move.isdigit() or not 1 <= int(move) <= 9:
            print("Please choose an available number from 1 to 9.")
            continue

        position = int(move) - 1
        if board[position] in ("X", "O"):
            print("That space is already taken. Choose another one.")
            continue

        return position


def play_game():
    """Run one game of Tic-Tac-Toe"""
    board = [str(number) for number in range(1, 10)]
    player = "X"

    print("\n=== Tic-Tac-Toe ===")
    print("Choose a space by entering its number:")
    display_board(board)

    for turn in range(9):
        position = get_move(board, player)
        board[position] = player
        display_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins!")
            return player

        if turn < 8:
            player = "O" if player == "X" else "X"

    print("It's a draw!")
    return None


def main():
    print("=== Tic-Tac-Toe Game ===")

    while True:
        print("\nOptions:")
        print("1. Play Tic-Tac-Toe")
        print("2. Exit")

        choice = input("\nEnter choice (1/2): ")

        if choice == "1":
            play_game()
            again = input("\nPlay again? (y/n): ").lower()
            if again != "y":
                print("Thanks for playing!")
                break
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()