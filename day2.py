# Passing by value Vs passing by Ref

# define a doubling function that passes args by value
def mult2(x):
    return x * 2

# define a doubling function that passes args by reference
def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2


# # try out the functions
# a = 12

# new_number = mult2(a)
# print(new_number)

# lst = [2, 4, 6, 8] # mutable
# mult2_list(lst)

# for num in lst:
#     print(num)













#===========================================================

# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
# except ignoring the largest and smallest values in the array. 

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5 (1 + 5 + 5 + 8 + 7) // 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

# UNDERSTAND

# how many integers to work with? (min 3 ints)
# if there are more than 1 largest or smallest value what do we do? we remove only 1
# do we need to account for floating points in our answers? no we only want to use int answers //


# PLAN & EXECUTE

def centered_avg1(ints):
    # use min and max to find the smallest and largest numbers
    # set smallest to the min of ints
    smallest = min(ints)
    # set largest to the max of ints
    largest = max(ints)

    # sum up the ramaining numbers minus the smallest and largest ones
    
    # set a value of zero to a sum variable to track the total
    sum = 0
    # iterate over the ints adding them to sum
    for i in ints:
        sum += i
    # set the sum to the sum minus the smallest and largest number
    sum = sum - smallest - largest
    

    
    # use a floor division to makesure no floats and return the result
    # return the sum divided by the length of ints minus 2
    return sum // (len(ints) - 2)

# use the stastistics module to give us the mean method on a sorted list

def centered_avg2(ints):
    # sort the ints
    #
    
    pass

numbers = [1, 41, 34, 29, 50, 50]

print(centered_avg1(numbers))
# a = 41 + 34 + 29 + 50
# print(a)

# b = a // 4

# print(b)


