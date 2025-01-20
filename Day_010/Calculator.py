def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print('''
 _____________________
|  _________________  |
| | Landry  Houston | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|      
''')

def calculator():
    total = float(input("What's the first number?: "))
    while True:
        for operator in operations:
            print(operator)
        operation_symbol = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        answer = operations[operation_symbol](total, second_number)
        print(f"{total} {operation_symbol} {second_number} = {answer}")
        
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if choice == 'y':
            total = answer
        else:
            break
    print(f"\n{"_"*10} New Calculation {"_"*10}\n")
    calculator()

calculator()