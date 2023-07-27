from typing import Literal

Symbol = Literal["X", "O"]


class Player:
    def __init__(self, name, symbol: Symbol):
        if symbol not in ["X", "O"]:
            raise ValueError("Symbol must be 'X' or 'O'")

        self.name = name
        self.symbol = symbol
