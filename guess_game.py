import random


def guess_number():
    target = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess > target:
            print("Too low! Try again.")
        elif guess < target:
            print("Too high! Try again.")
        else:
            if attempts > 50:
                print("Sorry, you've exceeded the maximum number of attempts. You lose!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
            break


if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number()