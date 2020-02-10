# This is a comment

# lets print a string

print("Hello, World!")

# variables
name = "Tom"
age = 40

print("Hello, " + name)

# f strings
name = "Bob"
print(f"Hello, {name}")

# collections

# create an empty list?
lst1 = [] # lst1 = list()

# create a list with numbers 1, 2, 3, 4, 5
lst2 = [1, 2, 3, 4, 5]

# add an element 24 to lst1
lst1.append(24)

# print all values in lst2
for n in lst2:
    print(n)

for (i, n) in enumerate(lst2):
    print(f"Element {i} is {n}")

# while loop

i = 0

while i < len(lst2):
    print(lst2[i])
    i += 1

# List Comprehensions

# Create a new list containing the squares of all values in 'numbers'
numbers = [1, 2, 3, 4, 5]
print(numbers)

squares = [n**2 for n in numbers]

print(squares)

squares = [num * num for num in numbers]
squares = [1, 4, 9, 16, 25]

print(squares)


squares = []
for num in numbers:
    squares.append( num * num )

print(squares)

# Filtering with a list comprehension

# create a new list of even numbers using the values of the numbers list as inputs
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [n for n in numbers if n % 2 == 0]

print(evens)

evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

print(evens)

# create a new list containing only the names that start with 's' make sure they are capitalized (regardless of their original case)

names = ['Patrick', 'Melquisedeque', 'Bob', 'steve', 'Sam', 'frank', 'shawn']

s_names = [name.capitalize() for name in names if name[0].lower() == 's']

print(s_names)


# Dictionaries

# Create a new dictionary
d1 = dict()
d1 = {}

d2 = { 'name': 'Tom', 'age': 40 }

# access an element via its key
print(d2['name'])

# iterate over dict

for key in elem:
    print(f'{key} is {elem[key]}')

for (k, v) in d2.items():
    print(k)
    print(v)




























