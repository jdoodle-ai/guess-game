import random

def main_game_loop():
    print("Welcome to the Number Guessing Game!")
    while True:
        difficulty = choose_difficulty()
        play_game(difficulty)
        if not play_again():
            break
    print("Thanks for playing!")

def choose_difficulty():
    while True:
        choice = input("Choose difficulty (1: Easy, 2: Medium, 3: Hard): ").strip()
        if choice in ['1', '2', '3']:
            return int(choice)
        print("Invalid choice. Please enter 1, 2, or 3.")

def play_game(difficulty):
    difficulty_settings = {
        1: (1, 50, 10),  # Easy: 1-50, 10 attempts
        2: (1, 100, 8),  # Medium: 1-100, 8 attempts
        3: (1, 200, 6)   # Hard: 1-200, 6 attempts
    }
    min_num, max_num, max_attempts = difficulty_settings[difficulty]
    target = random.randint(min_num, max_num)
    attempts = 0

    while attempts < max_attempts:
        guess = get_valid_input(min_num, max_num)
        attempts += 1
        result = check_guess(guess, target)
        if result == 0:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            score = calculate_score(attempts, difficulty)
            display_score(score)
            return
        provide_feedback(result, attempts, max_attempts)
    print(f"The number was {target}. Better luck next time!")

def get_valid_input(min_num, max_num):
    while True:
        try:
            guess = int(input(f"Guess a number between {min_num} and {max_num}: "))
            if min_num <= guess <= max_num:
                return guess
            print(f"Please enter a number between {min_num} and {max_num}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def check_guess(guess, target):
    if guess < target:
        return -1
    elif guess > target:
        return 1
    return 0

def provide_feedback(result, attempts, max_attempts):
    if result == -1:
        print("Too low!")
    else:
        print("Too high!")
    
    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"You have {remaining} attempts left.")
    
    if abs(result) == 1:
        print("You're getting warmer!")
    elif abs(result) == 2:
        print("You're very close!")

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        print("Invalid input. Please enter 'yes' or 'no'.")

def calculate_score(attempts, difficulty):
    base_score = 1000
    difficulty_multiplier = difficulty * 0.5
    return int(base_score * difficulty_multiplier / attempts)

def display_score(score):
    print(f"Your score: {score} points")

if __name__ == "__main__":
    main_game_loop()
