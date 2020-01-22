import pygame
import time
import Board

class Game():

    def __init__(self,  row, col):
        self.row = row
        self.col = col
        self.size = (700, 500)
        self.playing = True



    """ Initalises the sudoku game"""
    def start_game(self):
        pygame.init()

        # Open a new window
        pygame.display.set_mode(self.size)
        pygame.display.set_caption("Sudoku with Auto Solve")
        #game_board = Board.Board(self.row, self.col, window)
        
        pygame.display.update()

        
        
    def run_game(self):
        self.start_game()
        
        while(self.playing):
            event = pygame.event.wait()
            if event.type == pygame.quit():
                self.playing = False
            # self.playing = False

        pygame.quit()