def greet(name):
    return f" Hello, {name}!"

# code to execute when the module is run as script

if __name__ == "__main__":
# the block will only run if this file is executed directly
    print("Executing mymodule as a script.")
    name = "World"
    print(greet(name))

