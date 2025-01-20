bidders = {}

while True:
    while True:
        name = input("What is your name?: ")
        if name:
            break
    while True:
        try:
            bid_amount = float(input("What is your bid?: $"))
        except:
            continue
        break
    bidders[name] = bid_amount
    if input("Are there any other bidders? (yes/no).\n") != 'yes':
        break

max_key = None
max_value = 0
for key, value in bidders.items():
    if value > max_value:
        max_value = value
        max_key = key

if max_value.is_integer():
    print(f"The winner is {max_key} with a bid of ${int(max_value)}")
else:
    print(f"The winner is {max_key} with a bid of ${round(max_value, 1)}")