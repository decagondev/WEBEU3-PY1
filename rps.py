import random
# create a r/p/s game

# AI to be used (eg random selection)
# keep track of the score
# Rules: r beats s, s beats p, p beats r

# keep track of wins, losses and ties
win_count = 0
loss_count = 0
tie_count = 0
# hold the r, p s in a choices list
choices = ['r', 'p', 's']
# REPL
while True:
    # print the score
    print(f'Score: {win_count} - {loss_count} - {tie_count}')
    # Take input from user
    cmd = input('\nChose r/p/s: ')
    # AI picks a choice using a random range to index in to the choices list
    computer_choice = choices[random.randrange(3)]
    # print the AI choice
    print(f'Computer chose {computer_choice}')
    
    # some logic for the commands
    if cmd == 'r':
        if computer_choice == 'p':
            # loss
            loss_count += 1
            print('You Lose!')
        elif computer_choice == 's':
            # win
            win_count += 1
            print('You Win!')
        elif computer_choice == 'r':
            # tie
            tie_count += 1
            print("You Tie!")
    elif cmd == 'p':
        if computer_choice == 's':
            # loss
            loss_count += 1
            print('You Lose!')
        elif computer_choice == 'r':
            # win
            win_count += 1
            print('You Win!')
        elif computer_choice == 'p':
            # tie
            tie_count += 1
            print("You Tie!")
    elif cmd == 's':
        if computer_choice == 'r':
            # loss
            loss_count += 1
            print('You Lose!')
        elif computer_choice == 'p':
            # win
            win_count += 1
            print('You Win!')
        elif computer_choice == 's':
            # tie
            tie_count += 1
            print("You Tie!")
    elif cmd == 'q':
        print('Goodbye!')
        break
    else:
        print('I do not understand that command!')

        