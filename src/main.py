import pygame
import sys
from const import *
from game import Game


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):
        game = self.game
        screen = self.screen
        dragger = self.game.dragger
        board = self.game.board

        while True:
            game.show_bg(screen)
            game.show_pieces(screen)

            for event in pygame.event.get():

                if event.type == pygame.event.get():
                    # click
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        dragger.Update_mouse(event.pos)

                        clicked_row = dragger.mousey // sqsize
                        clicked_col = dragger.mousex // sqsize

                        print(dragger.mousey, clicked_row)
                        print(dragger.mousex, clicked_col)

                        # if clicked square has a piece ?
                        if board.squares[clicked_row][clicked_col].has_piece():
                            pass


                    # mouse motion
                    elif event.type == pygame.MOUSEMOTION:
                        pass

                    # CLICK REALISE
                    elif event.type == pygame.MOUSEBUTTONUP:
                        pass

                # QUIT THE APPLICATION
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
