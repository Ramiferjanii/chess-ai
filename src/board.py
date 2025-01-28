from const import *
from square import Square


class Board:
    def __init__(self):
        self.squares = [(0, 0, 0, 0, 0, 0, 0, 0) for col in range(cols)]
        self._create()

    # we pu '_' after name of  the function because i show to this methods is private methods
    def _create(self):
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        pass
