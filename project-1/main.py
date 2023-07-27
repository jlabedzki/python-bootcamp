from player import Player
from game import Game


def main():
    p1 = Player("Player 1", "X")
    p2 = Player("Player 2", "O")

    game = Game(p1, p2)

    welcome_and_instructions()

    while not game.game_over and not game.tie:
        game.display_board()
        choice = get_input(game.current_player)
        game.update_board(choice)
        game.change_turn()
        clear_output()

    if game.tie:
        print("It's a tie!")
    else:
        print(f'{game.winner.name} wins!')
        
    return


def welcome_and_instructions():
    print("Welcome to Tic Tac Toe!\nPlayer 1 will be X and Player 2 will be O\nTo make a move, enter a number from 1-9, where 1 is the top left corner and 9 is the bottom right corner\nThe first player to get 3 in a row wins!\nHere is the board:\n")


def get_input(player):
    try:
        choice = int(input(f"{player.name}: Enter a number from 1-9: "))
        if choice < 1 or choice > 9:
            raise ValueError
        return choice
    except ValueError:
        print("Invalid input, try again")
        return get_input(player)
    
def clear_output():
    print("\n" * 100)


if __name__ == "__main__":
    main()
