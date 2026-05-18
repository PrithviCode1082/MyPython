import random

chances = 10
number = random.randint(0, 100)

for i in range(0, chances):
    guess = int(input("Guess a number between 0 and 100: "))
    if(guess == number):
        print("You guessed correct!")
        break
    elif(guess > number):
        print("Guess a bit lower!")
    else:
        print("Guess a bit higher!")
