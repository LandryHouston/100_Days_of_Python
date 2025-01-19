import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '=', '?']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #[str(i) for i in range(0, 10)]


print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password = []

for i in range(1, num_letters + 1):
    password.append(random.choice(letters))
for i in range(1, num_symbols + 1):
    password.append(random.choice(symbols))
for i in range(1, num_numbers + 1):
    password.append(random.choice(numbers))

random.shuffle(password)
print(f"Your password is: {''.join(password)}")