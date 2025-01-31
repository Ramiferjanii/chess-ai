import pygame
from const import *
from board import Board
from dragger import  Dragger

class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

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

    def show_pieces(self, surface):
        for row in range(rows):
            for col in range(cols):
                # check piece ?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece


                    # all pieces except dragger piece
                    if piece is not self.dragger.piece :
                        piece.set_texture(size=80)

                        img = pygame.image.load(piece.texture)
                        img_center = col * sqsize + sqsize // 2, row * sqsize + sqsize // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self , surface):
        if self.dragger.dragging :
            piece = self.dragger.piece

            # loop all valid moves
            for move in piece.moves :
                #color
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                # rect
                rect = (move.final.col * sqsize  , move.final.row * sqsize , sqsize , sqsize)
                #blit
                pygame.draw.rect(surface, color, rect)

