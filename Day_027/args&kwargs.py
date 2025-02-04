def add(*args):
    return sum(args)

print(add(2, 3, 5))



def calculate(n, **kwargs):
    print(n, kwargs)
    
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
    
calculate(2, add=3, multiply=4)


class Car:
    
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
        
my_car = Car(make='GMC', model='Sierra 1500', color='Red')
print(my_car.color, my_car.model)