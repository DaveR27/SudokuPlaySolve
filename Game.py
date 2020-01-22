import pygame
import Game


class Board():
    BOARD = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    def __init__(self, row, col, window):
        self.row = row
        self.col = col
        self.window = window
        self.game_surface = [][]

    def create_board(self):
        for i in self.row:
            for j in self.col:
                self.game_surface[i][j] = Square(i, j, self.BOARD[i][j])


        
    def draw_board(self):
        pygame.draw.rect(self.window, self.BLACK, (4,4))



class Square():
    def __init__(self, row, col, num):
        self.row = row
        self.col = col
        self.num = num

