import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

hangman_logo = r"""
 _                                            
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

words = ['alpaca', 'forklift', 'cookie', 'computer', 'diamond', 'voodoo']

word_to_guess = random.choice(words)

print(hangman_logo)
print(f"Word to guess: {'_' * len(word_to_guess)}")

game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        continue
    correct_letters.append(guess)
    display =""
    for letter in word_to_guess:
        if letter == guess:
            display += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    if guess not in word_to_guess:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        if lives == 0:
            game_over = True
            print(stages[lives])
            print(f"{'*'*20} Game over! The word was {word_to_guess} {'*'*20}")
    if "_" not in display:
        game_over = True
        print(display)
        print("You win!")
    if game_over == False and lives > 0:
        print(display)
        print(stages[lives])
        print(f"{'*'*20} {lives}/6 LIVES LEFT {'*'*20}")
        print("Word to guess:", display)