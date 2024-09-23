# creating a set of  fruits

fruits = {"apple", "banana", "orange"}

#adding an element to set

fruits.add("grape")
print(fruits)

# remove banana
fruits.remove("banana")
print(fruits)

# checking if an element from set

print("Is 'apple' in the set?", "apple" in fruits)
print("Is 'banana' in the set?", "banana" in fruits)
print(fruits)

#length of set
length_fruits = len(fruits)
print(length_fruits)

# looping through set
print("set elements:")
for fruit in fruits:
    print(fruit)

# List of dictionaries representing students' information
students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "C"},
    {"name": "David", "age": 23, "grade": "B"}
]


# Accessing and manipulating individual records
print(students[0]["name"])  # Accessing the name of the first student
students[1]["age"] = 24  # Modifying the age of the second student

# Adding a new student record to the list
new_student = {"name": "Eva", "age": 19, "grade": "A"}
students.append(new_student)

# Iterating through the list of students
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")


