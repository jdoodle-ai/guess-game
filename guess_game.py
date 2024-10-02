import random


def guess_number():
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 8

    while attempts < max_attempts:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < target:
            print("Too low! Try again.")
        elif guess > target:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
    else:
        print("You suck at this! Try harder next time.")


if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number()