
## guessing game where user thinks of a number between 1 and 100
## and the program tries to guess it

## print the rules of the game
print("Think of a number between 1 and 100, and I will guess it.")
print("You have to tell me if my guess is less than, greater than or equal to your number.")

# set a sentinal value to exit loop
correct = False
# set the top and bottom bounds
top = 100
bottom = 1


## REPL
## continue looping until a condition is false
while not correct:
    ## have the computer guess the number
    guess = (top + bottom) // 2
    ## print our some prompt
    print(f"I am guessing it is {guess}")


    ## take input from user
    result = input("Less, Greater, or Equal? ").lower()
    result = result[0]

    ## evaluate input
    if result == 'l':
        top = guess - 1
    elif result == 'g':
        bottom = guess + 1
    elif result == 'e':
        correct = True
    else:
        print("Please enter either less, greater or equal")

    if top == bottom:
        guess = top
        correct = True

## print result
print(f'\nIt is {guess}!\n')
