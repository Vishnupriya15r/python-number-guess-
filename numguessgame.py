import random

print("🎯 Welcome to the Number Guessing Game! 🎯")

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7  # limit attempts

print("I have chosen a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it. Good luck! 🍀")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("📉 Too low! Try again.")
        else:
            print("📈 Too high! Try again.")

        print(f"Attempts left: {max_attempts - attempts}")

    except ValueError:
        print("⚠️ Please enter a valid number.")

if attempts == max_attempts and guess != secret_number:
    print(f"😢 Game Over! The number was {secret_number}.")
