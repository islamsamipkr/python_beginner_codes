# Import Python's random module
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Create a variable to store the user's guess
guess = 0

# Keep running until the user guesses correctly
while guess != secret_number:

    # Ask the user for a number
    guess = int(input("Guess a number between 1 and 10: "))

    # Check if their number is too low
    if guess < secret_number:
        print("Too low! Try again.")

    # Check if their number is too high
    elif guess > secret_number:
        print("Too high! Try again.")

    # Otherwise it must be correct
    else:
        print("Correct! 🎉")

# This executes after the while loop finishes
print("The secret number was", secret_number)
