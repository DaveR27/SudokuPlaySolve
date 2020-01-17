import pygame
import time

class Game():
    def __init__(self):
        # Define some colors
        self.black = ( 0, 0, 0)
        self.white = ( 255, 255, 255)
        self.green = ( 0, 255, 0)
        self.red = ( 255, 0, 0)
        self.size = (700, 500)
        self.playing = True


    """ Initalises the sudoku game"""
    def init_game(self):
        pygame.init()

        # Open a new window
        screen = pygame.display.set_mode(self.size)
        time.sleep(3)
        pygame.display.set_caption("Sudoku with Auto Solve")
        pygame.display.update()
        

    def run_game(self):
        self.init_game()
        

        while(self.playing):
            time.sleep(3)
            if event.type == pygame.QUIT:
                self.playing = False
            self.playing = False

        pygame.quit()