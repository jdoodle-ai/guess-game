import random

def initialize_game(difficulty):
    """Initialize game parameters based on difficulty."""
    if difficulty == 'easy':
        return 1, 50, 10
    elif difficulty == 'medium':
        return 1, 100, 8
    else:  # hard
        return 1, 200, 6

def get_valid_input(min_val, max_val):
    """Get and validate user input."""
    while True:
        try:
            guess = int(input(f"Guess a number between {min_val} and {max_val}: "))
            if min_val <= guess <= max_val:
                return guess
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def provide_feedback(guess, target):
    """Provide feedback and hints on the guess."""
    if guess < target:
        if target - guess > 20:
            return "Too low! Try a higher number."
        else:
            return "Getting warmer! Try a bit higher."
    elif guess > target:
        if guess - target > 20:
            return "Too high! Try a lower number."
        else:
            return "Getting warmer! Try a bit lower."
    else:
        return "Congratulations! You guessed it!"

def calculate_score(attempts, max_attempts, difficulty):
    """Calculate the player's score."""
    base_score = 1000
    difficulty_multiplier = {'easy': 1, 'medium': 1.5, 'hard': 2}
    return int(base_score * (max_attempts - attempts + 1) / max_attempts * difficulty_multiplier[difficulty])

def play_again():
    """Ask if the user wants to play again."""
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')

def display_difficulty_menu():
    """Display and handle difficulty selection."""
    print("\nSelect difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 8 attempts)")
    print("3. Hard (1-200, 6 attempts)")
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            return 'easy'
        elif choice == '2':
            return 'medium'
        elif choice == '3':
            return 'hard'
        else:
            print("Invalid choice. Please try again.")

def guess_number():
    """Main game function."""
    difficulty = display_difficulty_menu()
    min_val, max_val, max_attempts = initialize_game(difficulty)
    target = random.randint(min_val, max_val)
    attempts = 0

    while attempts < max_attempts:
        guess = get_valid_input(min_val, max_val)
        attempts += 1
        feedback = provide_feedback(guess, target)
        print(feedback)
        if guess == target:
            score = calculate_score(attempts, max_attempts, difficulty)
            print(f"You guessed it in {attempts} attempts. Your score: {score}")
            return
    
    print(f"Sorry, you've run out of attempts. The number was {target}.")
    print("Don't give up! You can do better next time.")

def main():
    """Main game loop."""
    print("Welcome to the Number Guessing Game!")
    while True:
        guess_number()
        if not play_again():
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
