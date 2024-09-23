# creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
print(empty_list)
print(numbers)

# mixed data
mixed_list = [1, 'hello', 3.14, True]
print(mixed_list)


# access first element of list

first_element = numbers[0]
third_element = numbers[2]
last_element =  numbers[-1]

print("first element:", first_element)
print("third element:", third_element)
print("last element:", last_element)

# modify the elements

numbers[0] = 10
numbers[2] = 30
numbers[-1] = 50
print(numbers)

#append

numbers.append(6)
print(numbers)

# insert at location

numbers.insert(2, 2.5)
print(numbers)

# add multiple elements
numbers.extend([237, 54, 67])
print(numbers)


#remove elements from list
numbers.remove(30)   #by elements
popped_element = numbers.pop(2) #by index
print(numbers)

#slice the list
numbers1 = [1, 2, 3, 4, 5]
first_three = numbers1[:3]
middle_two = numbers1[1:3]
last_two = numbers1[-2:]

print("first three elements:",first_three)
print("middle two elements:", middle_two)
print("last two elements:", last_two)

# iteration over a list
for num in numbers1:
    print(num)

    #list comprehension
squares =[x**2 for x in range(6)]
print(squares)









