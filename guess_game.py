import random


def guess_number():
    target = random.uniform(0, 100)
    attempts = 0

    while True:
        guess = float(input("Guess a number between 0 and 100: "))
        attempts += 1

        if guess > target:
            print("Too low! Try again.")
        elif guess < target:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break


if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number()