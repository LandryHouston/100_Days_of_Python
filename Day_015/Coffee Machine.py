menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * .25
    dimes = int(input("How many dimes?: ")) * .10
    nickles = int(input("How many nickles?: ")) * .05
    pennies = int(input("How many pennies?: ")) * .01
    total = quarters + dimes + nickles + pennies
    return total

def report():
    print(f'Water: {resources['water']}ml')
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    
def use_resources(coffee):
    for ingredient, amount in menu[coffee]['ingredients'].items():
        if ingredient in resources and resources[ingredient] >= amount:
            resources[ingredient] -= amount
        else:
            print(f"Not enough {ingredient}.")
            return False
    return True

def vend(total, choice):
    cost = menu[choice]['cost']
    if total == cost:
        pass
    elif total > cost:
        print(f"Here is your ${total - cost:.2f} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")
        return

    print(f"Here is your {choice} ☕ Enjoy!")
    resources['money'] += cost

def order():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == 'report':
            report()
        elif choice == 'off':
            is_on = False
        else:
            if use_resources(choice) == False:
                continue
            total = coins()
            vend(total, choice)

order()