import pygame
from const import *
from board import Board

class Game:
    def __init__(self):
        self.board = Board()

    # show methods
    def show_bg(self, surface):
        for row in range(rows):
            for col in range(cols):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)  #light screen
                else:
                    color = (119, 154, 88)  # dark green

                rect = (col * sqsize, row * sqsize, sqsize, sqsize)
                pygame.draw.rect(surface, color, rect)

    def show_pieces(self , surface):
        for row in range(rows):
            for col in range(cols):
                # check piece ?
                if self.board.squares[row][col].has_piece() :
                    pass

