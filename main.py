# GUI.py
import pygame
import time
import Game
pygame.init()

def main():
    row = 9
    col = 9
    window = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Sudoku Solver")
    playing = True
    Game.Board(row, col, window)
    start = time.time()
    while playing:

        play_time = round(time.time() - start)

        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()


main()
pygame.quit()