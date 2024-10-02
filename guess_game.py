import random


def guess_number():
    target = random.randint(1, 100)
    attempts = 0
    previous_score = float('inf')

    while True:
        print(f"Your target score is {previous_score}.")
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
            else:
                print("You lost! Sorry you are bad at this game.")
                break


if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number()