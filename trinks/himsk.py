import random


number_list = [5, 12, 25, 33, 47, 59, 66, 78, 84, 91]


chosen_number = random.choice(number_list)


print("Guess the number from this list:")
print(number_list)


guess = int(input("Enter your guess: "))


if guess == chosen_number:
    print("🎉 Correct! You guessed the right number!")
elif guess > chosen_number:
    print("❌ Too high! Try a smaller number.")
else:
    print("❌ Too low! Try a bigger number.")


print(f"The judge's number was: {chosen_number}")