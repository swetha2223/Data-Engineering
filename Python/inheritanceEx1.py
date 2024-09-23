class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):  # self will never be a parameter
        pass


#derived class (child  class) inheriting from animal

class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):

    def speak(self):
        return "Meow!"

# creating instance of derived class
dog = Dog("Buddy")
cat = Cat("Whiskers")
# creating the speak method on instance

print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")

