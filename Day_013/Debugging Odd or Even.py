# ORIGINAL CODE:
def odd_or_even(number):
    if number % 2 = 0:
        return "This is an even number."
    else:
        return "This is an odd number."
    
# FIXED CODE
def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
    
# The problem is 'if number % 2 = 0' It should be '=='.