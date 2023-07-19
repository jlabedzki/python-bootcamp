def main():
    print(welcome_and_instructions())
    print(make_board([' ' for _ in range(9)]))

# Entries is a list of 9 strings, each string is either ' ', 'X', or 'O'
def make_board(entries):
    return f'{entries[0]}|{entries[1]}|{entries[2]}\n-----\n{entries[3]}|{entries[4]}|{entries[5]}\n-----\n{entries[6]}|{entries[7]}|{entries[8]}'

def welcome_and_instructions():
    return 'Welcome to Tic Tac Toe!\nPlayer 1 will be X and Player 2 will be O\nTo make a move, enter a number from 1-9, where 1 is the top left corner and 9 is the bottom right corner\nThe first player to get 3 in a row wins!\nHere is the board:\n \n'

if __name__ == '__main__':
    main()