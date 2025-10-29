import random

secret = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

attempts = 0
for i in range(5) :
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if guess < 1 or guess > 100:
        print("Guess must be between 1 and 100.")
        continue

    attempts += 1

    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")
    else:
        print(f"Correct! You got it in {attempts} attempts.")
        break
else:
    print(f"Out of attempts! The number was {secret}.")