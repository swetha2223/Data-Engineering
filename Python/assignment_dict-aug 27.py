###Exercise 1: Create a Dictionary
#1. Create a dictionary called `person` with the following key-value pairs:
  # - Name: "Alice" , Age: 25 , City: "New York"
#2. Print the dictionary.

person = {"Name": "Alice", "Age": 25, "City": "New York"}
print(person)

###Exercise 2: Access Dictionary Elements
#1. Access the value of the "Name" key in the person dictionary and print it.

print(person["Name"])

#2. Access the value of the "City" key and print it.

print(person["City"])

###Exercise 3: Add and Modify Elements
#1. Add a new key-value pair to the `person` dictionary: `"email": "alice@example.com"`.

person["email"] = "alice@example.com"
#2. Change the value of the `"Age"` key to 26.

person["Age"] = 26
# 3. print the modified dictionary
print(person)

### Exercise 4: Remove Elements
#1. Remove the `"City"` key from the `person` dictionary. 2. Print the dictionary after removing the key.

del person["City"]
print(person)

### Exercise 5: Check if a Key Exists
#1. Check if the key `"email"` exists in the `person` dictionary. Print a message based on the result.

if "email" in person:
    print("Email key exists")
else:
    print("Email key does not exist")

#2. Check if the key `"phone"` exists in the dictionary. Print a message based on the result.

if "phone" in person:
    print("Phone key exists")
else:
    print("Phone key does not exist")

### Exercise 6: Loop Through a Dictionary
#1.Iterate over the `person` dictionary and print each key-value pair.

for key, value in person.items():
    print(key, ":", value)

#2. Iterate over the keys of the dictionary and print each key.

for key in person:
    print(key)
#3. Iterate over the values of the dictionary and print each value.

for value in person.values():
    print(value)

### Exercise 7: Nested Dictionary

employees = {
    101: {"name": "Bob", "job": "Engineer"},
    102: {"name": "Sue", "job": "Designer"},
    103: {"name": "Tom", "job": "Manager"}
}
print(employees[102])

employees[104] = {"name": "Linda", "job": "HR"}
print(employees)

### Exercise 8: Dictionary Comprehension
#1. Create a dictionary comprehension that generates a dictionary where the keys are numbers from 1 to 5 and the values are the squares of the keys. 2. Print the generated dictionary.

squares = {x: x**2 for x in range(1, 6)}
print(squares)

### Exercise 9: Merge Two Dictionaries
#1. Create two dictionaries: dict1 = {"a": 1, "b": 2}  dict2 = {"c": 3, "d": 4}
#2. Merge `dict2` into `dict1` and print the result.

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print(dict1)

#Exercise 10: Default Dictionary Values

map_letter_to_num = {"a": 1, "b": 2, "c": 3}
print(map_letter_to_num.get("b"))
print(map_letter_to_num.get("d", 0))

### Exercise 11: Dictionary from Two Lists

keys = ["name", "age", "city"]
values = ["Eve", 29, "San Francisco"]

person_new=dict(zip(keys,values))
print(person_new)

###Exercise12: Count Occurrences of Words

sentence = "the quick brown fox jumps over the lazy dog the fox"
count={}
for word in sentence.split():
    count[word]=count.get(word,0)+1
print(count)






