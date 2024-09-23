# base class (parent class)  # object of current class - self is used to represent the object inside the class


class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):  # self will never be a parameter
       # print("Animal speaks")
        pass


# creating  an instance - assigning a value  used to refer the object to outside the class
ani = Animal("bull")
ani.speak()

#derived class (child  class) inheriting from animal

class Dog(Animal):
    def speak(self):
        return "Woof!"

# creating instance of derived class
dog = Dog("Buddy")

# creating the speak method on instance

print(f"{dog.name} says: {dog.speak()}")






