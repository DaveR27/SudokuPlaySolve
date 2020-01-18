import pygame
import time

class Game():
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    def __init__(self):
        
        self.size = (700, 500)
        self.playing = True


    """ Initalises the sudoku game"""
    def init_game(self):
        pygame.init()

        # Open a new window
        pygame.display.set_mode(self.size)
        pygame.display.set_caption("Sudoku with Auto Solve")
        pygame.display.update()
        
        
    def run_game(self):
        self.init_game()
        

        while(self.playing):
            event = pygame.event.wait()
            if event.type == pygame.quit():
                self.playing = False
            # self.playing = False

        pygame.quit()