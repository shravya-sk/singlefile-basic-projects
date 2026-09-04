# Quiz Game
# Test your knowledge with an interactive quiz

def get_quiz_questions():
    """Return a list of quiz questions with answers and options"""
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
            "correct": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
            "correct": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
            "correct": "D"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A) Jane Austen", "B) William Shakespeare", "C) Mark Twain", "D) Charles Dickens"],
            "correct": "B"
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
            "correct": "C"
        },
        {
            "question": "In what year did the Titanic sink?",
            "options": ["A) 1912", "B) 1920", "C) 1905", "D) 1915"],
            "correct": "A"
        },
        {
            "question": "What is the chemical symbol for Gold?",
            "options": ["A) Go", "B) Gd", "C) Au", "D) Ag"],
            "correct": "C"
        },
        {
            "question": "Which country has the most population?",
            "options": ["A) India", "B) United States", "C) Indonesia", "D) Brazil"],
            "correct": "A"
        },
        {
            "question": "What is the speed of light?",
            "options": ["A) 300,000 km/s", "B) 150,000 km/s", "C) 450,000 km/s", "D) 200,000 km/s"],
            "correct": "A"
        },
        {
            "question": "How many strings does a violin have?",
            "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
            "correct": "A"
        }
    ]
    return questions

def display_question(question_num, question, options):
    """Display a question and its options"""
    print(f"\nQuestion {question_num}: {question}")
    for option in options:
        print(f"  {option}")

def get_user_answer():
    """Get and validate user answer"""
    while True:
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        else:
            print("Invalid input! Please enter A, B, C, or D.")

def play_quiz():
    """Run the quiz game"""
    questions = get_quiz_questions()
    score = 0
    total = len(questions)
    
    print("=== Welcome to the Quiz Game ===")
    print(f"Answer {total} questions to test your knowledge!\n")
    
    for i, q in enumerate(questions, 1):
        display_question(i, q["question"], q["options"])
        user_answer = get_user_answer()
        
        if user_answer == q["correct"]:
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Incorrect. The correct answer is {q['correct']}")
    
    # Display results
    percentage = (score / total) * 100
    print(f"\n{'='*40}")
    print(f"Quiz Complete!")
    print(f"Your Score: {score}/{total} ({percentage:.1f}%)")
    print(f"{'='*40}")
    
    # Performance feedback
    if percentage == 100:
        print("🏆 Perfect score! You're a genius!")
    elif percentage >= 80:
        print("⭐ Excellent! Great job!")
    elif percentage >= 60:
        print("👍 Good! Keep learning!")
    else:
        print("📚 Keep practicing to improve your score!")

def main():
    print("=== Quiz Game ===\n")
    
    while True:
        print("Options:")
        print("1. Start Quiz")
        print("2. Exit")
        
        choice = input("\nEnter choice (1/2): ")
        
        if choice == '1':
            play_quiz()
            again = input("\nTake the quiz again? (y/n): ").lower()
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
