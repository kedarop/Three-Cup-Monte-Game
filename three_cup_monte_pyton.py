from random import shuffle

# Shuffles the list and returns it
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# Asks player to guess the index
def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Pick a number: 0, 1, or 2: ')
    return int(guess)

# Checks if the player's guess is correct
def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('🎉 Correct! You found the ball!')
    else:
        print('❌ Wrong guess!')
        print('Here was the list:', mylist)

# Set up the game list
game_list = ['', 'O', '']
shuffled_list = shuffle_list(game_list)
guess = player_guess()
check_guess(shuffled_list, guess)
