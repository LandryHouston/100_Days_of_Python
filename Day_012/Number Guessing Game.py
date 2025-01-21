import random

print(r"""
   ____                      _____ _            _   _                 _               
  / ___|_   _  ___ ___ ___  |_   _| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __ 
 | |  _| | | |/ _ / __/ __|   | | | '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ | '__|
 | |_| | |_| |  __\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __| |   
  \____|\__,_|\___|___|___/   |_| |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
  """)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100...")

number = random.randint(1, 100)
guesses = 0

while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        guesses = 10
        break
    elif difficulty == 'hard':
        guesses = 5
        break

while True:
    for i in range(1, guesses + 1):
        print(f"\nYou have {guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.\nGuess again.")
        elif guess < number:
            print("Too low.\nGuess again.")
        else:
            print(f"You got it! The answer was {number}.")
            break
        guesses -= 1
    else:
        print(f"\nYou've run out of guesses. The number was {number}.\nThanks for playing!")
        break
    if guess == number:
        break