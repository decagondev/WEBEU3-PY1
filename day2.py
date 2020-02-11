# Passing by value Vs passing by Ref

# define a doubling function that passes args by value
def mult2(x):
    return x * 2

# define a doubling function that passes args by reference
def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2


# try out the functions
a = 12

new_number = mult2(a)
print(new_number)

lst = [2, 4, 6, 8] # mutable
mult2_list(lst)

for num in lst:
    print(num)













#===========================================================

# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
# except ignoring the largest and smallest values in the array. 

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3
