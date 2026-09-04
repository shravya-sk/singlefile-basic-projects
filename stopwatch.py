# Stopwatch/Timer
# A simple stopwatch and timer application

import time

def stopwatch():
    """Run a stopwatch"""
    print("\n=== Stopwatch ===")
    print("Press Enter to start, then 's' to stop, or 'q' to quit\n")
    
    input("Press Enter to start...")
    start_time = time.time()
    
    while True:
        elapsed = time.time() - start_time
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed % 1) * 100)
        
        print(f"\rTime: {minutes:02d}:{seconds:02d}:{milliseconds:02d}", end='', flush=True)
        
        try:
            user_input = input()
            if user_input.lower() == 's':
                print(f"\nStopped at: {minutes:02d}:{seconds:02d}:{milliseconds:02d}")
                break
            elif user_input.lower() == 'q':
                return
        except:
            pass
        
        time.sleep(0.01)

def timer(seconds):
    """Run a countdown timer"""
    print(f"\n=== Timer: {seconds} seconds ===\n")
    
    start_time = time.time()
    
    while True:
        elapsed = time.time() - start_time
        remaining = seconds - elapsed
        
        if remaining <= 0:
            print("\n⏰ Time's up!")
            return
        
        minutes = int(remaining // 60)
        secs = int(remaining % 60)
        print(f"\rTime remaining: {minutes:02d}:{secs:02d}", end='', flush=True)
        
        time.sleep(0.1)

def main():
    print("=== Stopwatch & Timer ===\n")
    
    while True:
        print("Options:")
        print("1. Stopwatch")
        print("2. Timer")
        print("3. Exit")
        
        choice = input("\nEnter choice (1/2/3): ")
        
        if choice == '1':
            stopwatch()
        elif choice == '2':
            try:
                seconds = int(input("Enter timer duration in seconds: "))
                if seconds <= 0:
                    print("Please enter a positive number!")
                    continue
                timer(seconds)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
