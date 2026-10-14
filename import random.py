import random

print("Hello! Please choose a number from 1 to 10 and guess correctly.")

while True:
    random_number = random.randint(1, 10)
    try:
        guess = int(input("Enter Number: "))
    except ValueError:
        print("That is not a valid number. Please enter a number from 1 to 10.")
        continue

    if guess == random_number:
        print("Good job!")
        print("The number was:", random_number)
        break

    print("That's wrong. Try again.")