import random


def guess_number():
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    previous_score = float('inf')

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess > target:
            print("Too low! Try again.")
        elif guess < target:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            if attempts < previous_score:
                previous_score = attempts
                print(f"New best score! You beat your previous score of {previous_score} attempts.")
            else:
                print(f"You lost! You are bad at this game. You needed {previous_score} attempts to win.")
                break
            break
        if attempts >= max_attempts:
            print(f"You lost! You are bad at this game. You needed {previous_score} attempts to win.")
            break


if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number()