import random

secret = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10.")

attempts = 0
while True:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if guess < 1 or guess > 10:
        print("Guess must be between 1 and 10.")
        continue

    attempts += 1

    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")
    else:
        print(f"Correct! You got it in {attempts} attempts.")
        break