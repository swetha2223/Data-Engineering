#Exercise 1: Create a List
#Create a list called fruits with the following items: "apple", "banana", "cherry", "date", and "elderberry".
#Print the list.

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)

#Exercise 2: Access List Elements Print the first and last items from the fruits list.Print the second and fourth items from the list.
print( "first element:", fruits[0])
print("last element:", fruits[-1])
print("second element:",fruits[1])
print("fourth element:",fruits[3])

#Exercise 3: Modify a List Replace "banana" in the fruits list with "blueberry".

fruits[1] = "blueberry"
print(fruits)

#Exercise 4: Add and Remove Elements
#Append "fig" and "grape" to the fruits list. Remove "apple" from the list.

fruits.append("fig")
fruits.append("grape")
fruits.remove("apple")
print(fruits)

#Exercise 5: Slice a List
#Slice the first three elements from the fruits list and assign them to a new list called first_three_fruits.

first_three_fruits = fruits[:3]
print("First three fruits:", first_three_fruits)

#Exercise 6: Find List Length
#Find and print the length of the fruits list.

print(len(fruits))

#Exercise 7: List Concatenation
#Create a second list called vegetables with the following items: "carrot", "broccoli", "spinach". Concatenate the fruits and vegetables lists into a new list called food.

vegetables = ["carrot", "broccoli", "spinach"]
food = fruits + vegetables
print(food)

#Exercise 8: Loop Through a List
#Loop through the fruits list and print each item on a new line.

for fruit in fruits:
    print(fruit)

#Exercise 9: Check for Membership
#Check if "cherry" and "mango" are in the fruits list. Print a message for each check.

if "cherry" in fruits:
    print("Cherry is present")
else:
    print("Cherry is not present")
if "mango" in fruits:
    print("mango is present")
else:
    print("mango is not present")

#Exercise 10: List Comprehension
#Use list comprehension to create a new list called fruit_lengths that contains the lengths of each item in the fruits list.

fruit_lengths = [len(fruit) for fruit in fruits]
print(fruit_lengths)

#Exercise 11: Sort a List
#Sort the fruits list in alphabetical order and print it.
fruits.sort()
print(fruits)

#Sort the fruits list in reverse alphabetical order and print it.
fruits.sort(reverse=True)
print(fruits)

#Exercise 12: Nested Lists
#Create a list called nested_list that contains two lists: one with the first three fruits and one with the last three fruits.
#Access the first element of the second list inside nested_list and print it.
nested_list=[fruits[:3],fruits[-3:]]
print(nested_list[1][0])

#Exercise 13: Remove Duplicates
#Create a list called numbers with the following elements: [1, 2, 2, 3, 4, 4, 4, 5]. Remove the duplicates from the list and print the list of unique numbers.#
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)

# exercise:14 Split and Join Strings
#Split the string "hello, world, python, programming" into a list called words using the comma as a delimiter.

string = "hello,world,python,Programming"
split_string = string.split(",")
print(split_string)
#join the words list back into a string using a space as the separator and print it.

joined_string = ", ".join(split_string)
print(joined_string)













