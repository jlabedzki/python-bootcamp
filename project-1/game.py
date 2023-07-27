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
        print(f"{self.board[3]}|{self.board[4]}|{self.board[5]}")
        print(f"{self.board[6]}|{self.board[7]}|{self.board[8]}")
        print('\n')

    def update_board(self, choice: int):
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
            
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return True
            
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True
            

        return False
    
    @property
    def tie(self):
        if self.game_over:
            return False
        
        for entry in self.board:
            if entry == " ":
                return False
            
        return True
    
    @property
    def winner(self):
        if not self.game_over:
            return None 
            
        """
        Account for the fact that the game will change turns in the while loop
        after before checking if the game is over
        """
        if self.current_player == self.player1:
            return self.player2
        
        return self.player1
        
    
