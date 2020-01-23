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

        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
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
            if event.key == pygame.K_DELETE:
                # game_surface.clear()
                key_press = None

            if event.key == pygame.K_SPACE:
                pass


        pygame.display.update()


main()
pygame.quit()