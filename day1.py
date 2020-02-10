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






