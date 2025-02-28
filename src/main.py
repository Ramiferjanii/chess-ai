import pygame
import sys
from const import *
from game import Game
from square import Square
from move import Move

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
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_hover(screen)


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
                        #valid piece color
                        if piece.color == game.next_player :

                            board.calc_moves(piece , clicked_row , clicked_col)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            #show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)

                # Handle mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // sqsize
                    motion_col = event.pos[0] // sqsize
                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging :
                        dragger.update_mouse(event.pos)
                        # show methods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)


                # Handle mouse button up
                elif event.type == pygame.MOUSEBUTTONUP:

                    if dragger.dragging :
                        dragger.update_mouse(event.pos)
                        released_row =dragger.mousey // sqsize
                        released_col = dragger.mousex // sqsize


                        # create possible move
                        initial = Square(dragger.initial_row , dragger.initial_col)
                        final = Square(released_row , released_col)
                        move = Move(initial , final )

                        # valid move

                        if board.valid_move(dragger.piece , move) :
                            captured = board.squares[released_row][released_col].has_piece()
                            board.move(dragger.piece , move )
                            # sounds
                            game.play_sound()
                            # show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)
                            # next turn
                            game.next_turn()


                            # valid move
                    dragger.undrag_piece()

                # key press
                elif event.type  == pygame.KEYDOWN :
                    # change themes
                    if event.key == pygame.K_t :
                        game.change_theme()
                    # restart
                    if event.key == pygame.K_r :
                        game.reset()
                        game = self.game
                        dragger = self.game.dragger
                        board = self.game.board


                # Handle quit event
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
