
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



    def move(self , piece , move):
        initial = move.initial
        final = move.final


        #console board move update
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece


        # move
        piece.moved = True


        # clear valid moves
        piece.clear_moves()





    def valid_move(self , piece , move ):
        return move in piece.moves





    def calc_moves(self, piece, row, col):
        '''

        :param piece:
        :param row:
        :param col:
        :return:  calculate all the possible (valid ) moves of an specific piece ona a specific position

        '''

        def pawn_moves():
            # steps
            steps  = 1 if piece.moved else 2

            #vertical move
            start = row + piece.dir
            end = row + (piece.dir   * (1  + steps ) )
            for possible_move_row in range(start , end , piece.dir ) :
                if Square.in_range(possible_move_row) :
                    if self.squares[possible_move_row][col].isempty() :
                        #create initial and final move squares
                        initial = Square(row , col)
                        final = Square(possible_move_row , col )
                        move = Move(initial , final)
                        piece.add_move(move)
                    #get_blocked()
                    else : break
                else : break # not in range
            #digramme moves
            possible_move_row  = row + piece.dir
            possible_move_col = [col -1, col + 1]
            for possible_move_col in possible_move_col:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                        # create initial and final moves
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # create a new move
                        move = Move(initial, final)
                        #append new move
                        piece.add_move(move)

        def king_moves():
            adjs = [
                (row - 1, col),  # Up
                (row - 1, col + 1),  # Up-Right
                (row, col + 1),  # Right
                (row + 1, col + 1),  # Down-Right
                (row + 1, col),  # Down
                (row + 1, col - 1),  # Down-Left
                (row, col - 1),  # Left
                (row - 1, col - 1),  # Up-Left
            ]
            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    target_square = self.squares[possible_move_row][possible_move_col]
                    # CORRECTED: Check if square is empty OR has an enemy piece
                    if target_square.isempty() or target_square.has_enemy_piece(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        piece.add_move(move)



            # castling moves


            # queen casting


            # king casting




        def straightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.in_range(possible_move_row, possible_move_col):

                        # create squares of the possible new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # create ea possible new move
                        move = Move(initial, final)
                        # append new move

                        # empty = continue looping
                        if self.squares[possible_move_row][possible_move_col].isempty():
                            # create new move
                            piece.add_move(move)

                        # has enemy piece = add move + break
                        if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                            # create new move
                            piece.add_move(move)
                            break

                        #    has team piece
                        if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break

                    else:
                        break
                    # increementing incrs

                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr

        def knight_moves():
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
            for move in possible_moves:  # Rename loop variable
                possible_row, possible_col = move
                if Square.in_range(possible_row, possible_col):
                    target_square = self.squares[possible_row][possible_col]
                    if target_square.isempty_or_enemy(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_row, possible_col)
                        move = Move(initial, final)
                        piece.add_move(move)

        if isinstance(piece, Pawn):
            pawn_moves()
        elif isinstance(piece, Knight):
            knight_moves()
        elif isinstance(piece, Rook):
            straightline_moves([
                (-1, 0),  # Up
                (0, 1),  # Right
                (1, 0),  # Down
                (0, -1),  # Left
            ])
        elif isinstance(piece, Queen):
            straightline_moves(
                [(-1, 1),  # up right
                 (-1, -1),  # up left
                 (1, 1),  # down right
                 (1, -1),  # down left
                 (-1, 0),  # up
                 (0, 1),  # left
                 (1, 0),  # down
                 (0, -1),  # left
                 ])

        elif isinstance(piece, King):
            king_moves()




        elif isinstance(piece, Bishop):
            straightline_moves(
                [(-1, 1),  # up right
                 (-1, -1),  # up left
                 (1, 1),  # down right
                 (1, -1),  # down left
                 ]
            )

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

