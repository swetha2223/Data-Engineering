import mymodule

print(mymodule.greet("Abdullah"))

import math_operations
result = math_operations.add(5, 3)
print(result)

result1 =  math_operations.division(20, 2)
print(result1)


# using packages from mymodule package
from mypackage import arithmatic

from  mypackage import geometry

# accepting all package - refer init file
from mypackage import *


print("Addition:", arithmatic.add(10, 5))
print("Division:", arithmatic.division(10, 2))

# using geometry function
print("area of circle:", geometry.area_of_circle(5))
print("Perimeter of rectangle:", geometry.perimeter_of_rectangle(10, 5))


### key word argument
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")


# using keyword arguments
describe_pet(animal_type = "cat", pet_name = "Whiskers")
describe_pet(pet_name="Rover")

# as many parameters - arbitrary arguments - it is used when we dont know the number of arguments
def make_pizza(size, *toppings):
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

#calling with arbitrary positional arguments
make_pizza(12, "Pepperoni", "mushrooms", "green peppers")

# allocating a dictionary key word arguments - we cann pass as many objects we want

def build_profile(first, last, **user_info):
    return{"first_name":first, "last_name": last, **user_info}

#calling with arbitrary keyword arguments

user_profile = build_profile("john", "doe", location = "new york", field="Engineering")

print(user_profile)










