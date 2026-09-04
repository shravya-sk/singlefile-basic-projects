# Hangman Game
# Guess the word before you run out of attempts!

import random

def get_word_list():
    """Return a list of words for the game"""
    words = [
        "python", "javascript", "hangman", "computer", "programming",
        "algorithm", "function", "variable", "database", "network",
        "internet", "password", "encryption", "developer", "debugging",
        "framework", "library", "repository", "terminal", "keyboard",
        "monitor", "printer", "scanner", "router", "server",
        "cloud", "storage", "backup", "security", "firewall"
    ]
    return words

def display_hangman(tries):
    """Display hangman stages based on remaining tries"""
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |     
           |      
           |     
           -
        """
    ]
    return stages[tries]

def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def play_game():
    """Main game loop"""
    word = random.choice(get_word_list()).upper()
    word_length = len(word)
    guessed_letters = set()
    correct_letters = set()
    tries = 6
    guessed_words = []
    
    print("\n=== Welcome to Hangman ===")
    print(f"The word has {word_length} letters.")
    print("Guess letters or try to guess the whole word!")
    
    while tries > 0:
        print(display_hangman(tries))
        print(f"\nWord: {display_word(word, correct_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Tries remaining: {tries}")
        
        guess = input("\nGuess a letter or the whole word: ").upper()
        
        if not guess:
            print("Please enter something!")
            continue
        
        if len(guess) == 1:
            # Single letter guess
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'!")
                continue
            
            if not guess.isalpha():
                print("Please enter a valid letter!")
                continue
            
            guessed_letters.add(guess)
            
            if guess in word:
                correct_letters.add(guess)
                print(f"✓ Good guess! '{guess}' is in the word!")
                
                # Check if word is complete
                if correct_letters == set(word):
                    print(display_hangman(tries))
                    print(f"\n🎉 Congratulations! You guessed the word: {word}")
                    return True
            else:
                print(f"✗ Sorry! '{guess}' is not in the word.")
                tries -= 1
        
        else:
            # Whole word guess
            if guess in guessed_words:
                print("You already guessed that word!")
                continue
            
            guessed_words.append(guess)
            
            if guess == word:
                print(f"\n🎉 Congratulations! You guessed the word: {word}")
                return True
            else:
                print(f"✗ Sorry! '{guess}' is not the word.")
                tries -= 1
    
    print(display_hangman(tries))
    print(f"\n❌ Game Over! The word was: {word}")
    return False

def main():
    print("=== Hangman Game ===")
    
    while True:
        print("\nOptions:")
        print("1. Play Hangman")
        print("2. Exit")
        
        choice = input("\nEnter choice (1/2): ")
        
        if choice == '1':
            play_game()
            again = input("\nPlay again? (y/n): ").lower()
            if again != 'y':
                print("Thanks for playing!")
                break
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
