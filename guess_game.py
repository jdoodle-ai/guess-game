import random

def main():
    print("Welcome to the Number Guessing Game!")
    while True:
        difficulty = choose_difficulty()
        play_game(difficulty)
        if not play_again():
            break
    print("Thanks for playing!")

def choose_difficulty():
    while True:
        choice = input("Choose difficulty (1-Easy, 2-Medium, 3-Hard): ").strip()
        if choice in ['1', '2', '3']:
            return int(choice)
        print("Invalid choice. Please enter 1, 2, or 3.")

def play_game(difficulty):
    difficulty_settings = {
        1: (1, 50, 10),  # Easy: 1-50, 10 attempts
        2: (1, 100, 8),  # Medium: 1-100, 8 attempts
        3: (1, 200, 6)   # Hard: 1-200, 6 attempts
    }
    min_value, max_value, max_attempts = difficulty_settings[difficulty]
    target = random.randint(min_value, max_value)
    attempts = 0

    while attempts < max_attempts:
        guess = get_valid_guess(min_value, max_value)
        attempts += 1
        result = check_guess(guess, target)
        if result == 0:
            score = calculate_score(attempts, max_attempts, difficulty)
            print_result(attempts, max_attempts, score)
            return
        print(get_hint(guess, target, result))
    
    print(f"\nOut of attempts! The number was {target}.")
    print("Don't give up! You'll do better next time.")

def get_valid_guess(min_value, max_value):
    while True:
        try:
            guess = int(input(f"Guess a number between {min_value} and {max_value}: "))
            if min_value <= guess <= max_value:
                return guess
            print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def check_guess(guess, target):
    if guess < target:
        return -1
    elif guess > target:
        return 1
    return 0

def get_hint(guess, target, result):
    diff = abs(guess - target)
    if diff > 50:
        return "You're freezing cold!"
    elif diff > 20:
        return "You're getting warmer!"
    elif diff > 10:
        return "You're very close!"
    else:
        return "You're red hot!"

def print_result(attempts, max_attempts, score):
    print(f"\nCongratulations! You guessed it in {attempts} attempts.")
    print(f"Your score: {score} points")

def calculate_score(attempts, max_attempts, difficulty):
    base_score = (max_attempts - attempts + 1) * 100
    difficulty_multiplier = difficulty * 0.5
    return int(base_score * (1 + difficulty_multiplier))

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()