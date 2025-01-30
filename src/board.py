from const import *
from square import Square
from piece import *
from move import  *


class Board:
    def __init__(self):
        self.squares = [[None for _ in range(cols)] for _ in range(rows)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def calc_moves(self, piece, row, col):
        '''

        :param piece:
        :param row:
        :param col:
        :return:  calculate all the possible (valid ) moves of an specific piece ona a specific position

        '''

        def knight_moves():
            # 8 possible moves
            possible_moves = [
                (row - 2, col + 1),
                (row - 1, col + 2),
                (row + 1, col + 2),
                (row + 2, col + 1),
                (row + 2, col - 1),
                (row + 1, col - 2),
                (row - 1, col - 2),
                (row - 2, col - 1),

            ]
            for possible_moves in possible_moves:
                possible_moves_row, possible_moves_col = possible_moves
                if Square.in_range(possible_moves_row, possible_moves_col):
                    if self.squares[possible_moves_row][possible_moves_col].isempty_or_rival(piece.color):
                        # create squares of the new move
                        initial = Square(row , col )
                        final = Square(possible_moves_row , possible_moves_col ) #piece = piece
                        # create new moves
                        move = Move(initial , final)
                        # append new bool move
                        pass

        if isinstance(piece, Pawn):
            pass

        elif isinstance(piece, Knight):
            knight_moves()


        elif isinstance(piece, Rook):
            pass


        elif isinstance(piece, Queen):
            pass


        elif isinstance(piece, King):
            pass


        elif isinstance(piece, Bishop):
            pass

    # we put '_' after the name of the function to indicate that these methods are private
    def _create(self):
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        """    it's the same value
        if color == 'white':
                row_pawn, row_other = (6, 7)
            else:
                row_pawn, row_other = (1, 0)"""
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)
        # these are all pawns
        for col in range(cols):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
        # knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # king
        self.squares[row_other][4] = Square(row_other, 4, King(color))
