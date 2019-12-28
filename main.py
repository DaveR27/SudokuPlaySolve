import pygame

class Game():
    def __init__(self):
        # Define some colors
        self.black = ( 0, 0, 0)
        self.white = ( 255, 255, 255)
        self.green = ( 0, 255, 0)
        self.red = ( 255, 0, 0)
        self.size = (700, 500)


    """ Initalises the sudoku game"""
    def init_game(self):
        pygame.init()

        # Open a new window
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Sudoku with Auto Solve")


def main():
    sudoku = Game()