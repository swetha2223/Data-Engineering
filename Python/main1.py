# using formate() method
import args

greet ="Hello"
name="alice"
full=greet+", "+name+"!"
print(full)

# another form
FORMATT ="{}, {}!".format(  greet,name)
print(FORMATT)

FORMATT2 = f"{greet}, {name}!"
print(FORMATT2)

#
text = " Python Programming "

stripped_text = text.strip()
print(stripped_text)

uppercase_text = text.upper()
print(uppercase_text)

starts_with_python = text.startswith("Python")
print(starts_with_python)


replaced_text = text.replace("Programming","Coding")
print(replaced_text)

# integers

positive_int = 42
negative_int =-42
zero =0
print(positive_int)
print(negative_int)
print(zero)