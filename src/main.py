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
            # show methods
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)


            if dragger.dragging :
                dragger.update_blit(screen)

            for event in pygame.event.get():  # Directly iterate through events
                # Handle mouse button down
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mousey // sqsize
                    clicked_col = dragger.mousex // sqsize


                    #if clicked dsquare has a piece ?
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        board.calc_moves(piece , clicked_row , clicked_col)
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        #show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)

                # Handle mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging :
                        dragger.update_mouse(event.pos)
                        # show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        dragger.update_blit(screen)
                        game.show_pieces(screen)

                # Handle mouse button up
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                # Handle quit event
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
