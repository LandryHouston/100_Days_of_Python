from numpy import random

rock, paper, scissors = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_choice = random.randint(0, 3)

if int(player_choice) == 0:
    print(rock)
    print("Computer chose:")
    if computer_choice == 0:
        print(f"{rock}\nIt's a draw")
    elif computer_choice == 1:
        print(f"{paper}\nYou lose")
    else:
        print(f"{scissors}\nYou win!")
elif int(player_choice) == 1:
    print(paper)
    print("Computer chose:")
    if computer_choice == 0:
        print(f"{rock}\nYou win!")
    elif computer_choice == 1:
        print(f"{paper}\nIt's a draw")
    else:
        print(f"{scissors}\nYou lose")
elif int(player_choice) == 2:
    print(scissors)
    print("Computer chose:")
    if computer_choice == 0:
        print(f"{rock}\nYou lose")
    elif computer_choice == 1:
        print(f"{paper}\nYou win!")
    else:
        print(f"{scissors}\nIt's a draw")
else:
    print("You typed an invalid number, you lose!")