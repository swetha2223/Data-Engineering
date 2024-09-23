empty_dict = {}
person = {
    "name": "mark",
    "age": 30,
    "email": "mark@example.com"
}
print(empty_dict)
print(person)

#Accessing value
name = person["name"]
age = person["age"]
print("Name:", name)
print("age:", age)

#modify the values
person["age"] = 31
person["email"] = "mark_new@example.com"

print(person)

# add new element
person["address"] = "123 Main St"
print(person)

# delete
del person["email"]

print(person)

#key
keys = person.keys()
values = person.values()
items = person.items()

print("keys:", keys)
print("values:", values)
print("items:", items)

# iterating over keys
for key in person:
    print(key)

# iterating over values
for value in person.values():
    print(value)

# iterating over keys and values
for key, value in person.items():
    print(key, ":", value)






