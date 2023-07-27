from typing import List, Literal

BoardEntries = Literal[" ", "X", "O"]


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.board: List[BoardEntries] = [" " for _ in range(9)]

    def display_board(self):
        print(f"{self.board[0]}|{self.board[1]}|{self.board[2]}")
        # print("-----")
        print(f"{self.board[3]}|{self.board[4]}|{self.board[5]}")
        # print("-----")
        print(f"{self.board[6]}|{self.board[7]}|{self.board[8]}")

    def update_board(self, choice):
        if choice < 1 or choice > 9:
            raise ValueError("Choice must be between 1 and 9")
        self.board[choice - 1] = self.current_player.symbol

    def change_turn(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    @property
    def game_over(self):
        # Check rows
        for i in range(0, 3, 6):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != " ":
                return True

        return False
