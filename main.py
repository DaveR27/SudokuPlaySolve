# GUI.py
import pygame
import Game
pygame.init()

def main():
    row = 9
    col = 9
    square_dim = 720
    window = pygame.display.set_mode((square_dim,square_dim))
    pygame.display.set_caption("Sudoku Solver")
    playing = True
    key_press = None

    game_surface = Game.Board(row, col, square_dim, window)
    while playing:
        #adds to the board surface
        if game_surface.clicked_box and key_press != None:
            x, y = game_surface.clicked_box
            if game_surface.valid(x, y, key_press):
                game_surface.sketch(key_press)
                pygame.mouse.set_visible(True)
                key_press = None
                game_surface.clicked_box == None
            else:
                pygame.mouse.set_visible(True)
                key_press = None
                game_surface.clicked_box == None
                print("Not a valid move")
                

        #handles events on the GUI
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
            if event.key == pygame.K_1:
                key_press = 1
            if event.key == pygame.K_2:
                key_press = 2
            if event.key == pygame.K_3:
                key_press = 3
            if event.key == pygame.K_4:
                key_press = 4
            if event.key == pygame.K_5:
                key_press = 5
            if event.key == pygame.K_6:
                key_press = 6
            if event.key == pygame.K_7:
                key_press = 7
            if event.key == pygame.K_8:
                key_press = 8
            if event.key == pygame.K_9:
                key_press = 9
            # if event.key == pygame.K_DELETE:
            #     # game_surface.clear()
            #     key_press = None

        if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = game_surface.click(pos)
                if clicked:
                    pygame.mouse.set_visible(False)

        #handles the updating of the display after a move    
        game_surface.draw_grid()
        playing = game_surface.game_won(playing)
        pygame.display.update()


main()
pygame.quit()