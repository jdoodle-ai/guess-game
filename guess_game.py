import random


def guess_number():
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 0
    previous_score = float('inf')

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        max_attempts = max(max_attempts, attempts)

        if guess < target:
            print("Too low! Try again.")
        elif guess > target:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            if attempts < previous_score:
                previous_score = attempts
                print(f"New record! You beat your previous score of {max_attempts} attempts.")
            else:
                print(f"Not bad! You matched your previous score of {max_attempts} attempts.")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing! Goodbye!")
                break
            else:
                target = random.randint(1, 100)
                attempts = 0
                max_attempts = 0


if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number()