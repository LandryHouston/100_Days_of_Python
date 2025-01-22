from HL_Data import data
import random

higher = """
██╗  ██╗██╗ ██████╗ ██╗  ██╗███████╗██████╗ 
██║  ██║██║██╔════╝ ██║  ██║██╔════╝██╔══██╗
███████║██║██║  ███╗███████║█████╗  ██████╔╝
██╔══██║██║██║   ██║██╔══██║██╔══╝  ██╔══██╗
██║  ██║██║╚██████╔╝██║  ██║███████╗██║  ██║
╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""
lower = """
██╗      ██████╗ ██╗    ██╗███████╗██████╗ 
██║     ██╔═══██╗██║    ██║██╔════╝██╔══██╗
██║     ██║   ██║██║ █╗ ██║█████╗  ██████╔╝
██║     ██║   ██║██║███╗██║██╔══╝  ██╔══██╗
███████╗╚██████╔╝╚███╔███╔╝███████╗██║  ██║
╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
"""
vs = r"""
__     __
\ \   / /__
 \ \ / / __|
  \ V /\__ \_
   \_/ |___(_)
"""

def compare(score=0):
    a, b = [random.choice(data)], [random.choice(data)]
    while a == b:
        b = [random.choice(data)]
    print(higher, lower)
    print(f"Compare A: {a[0]['name']}, a {a[0]['description']}, from {a[0]['country']}.")
    print(vs)
    print(f"Against B: {b[0]['name']}, a {b[0]['description']}, from {b[0]['country']}.")
    
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    print(f"\n"*50)
    if answer == "a" and a[0]["follower_count"] > b[0]["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}")
        compare(score)
    elif answer == "b" and b[0]['follower_count'] > a[0]['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
        compare(score)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        if input("Play Again? (y/n): ").lower() == 'y':
            compare()
            
compare()