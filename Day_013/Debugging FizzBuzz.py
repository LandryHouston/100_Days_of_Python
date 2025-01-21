# ORIGINAL CODE:
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print([number])

# FIXED CODE
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0: # 'and' instead of 'or'
            print("FizzBuzz")
        elif number % 3 == 0:   # Change to elif
            print("Fizz")
        elif number % 5 == 0:   # Change to elif
            print("Buzz")
        else:
            print(number)   # Remove square brackets