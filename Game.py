import pygame
import Game

class Board():
    BOARD = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 3, 0]
    ]
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    def __init__(self, row, col, square_dim, window):
        pygame.font.init()
        self.row = row
        self.col = col
        self.square_dim = square_dim
        #how many number across the board is
        self.boxes_across = 9 
        self.window = window
        self.game_surface = [
            [Square(i,j,self.BOARD[i][j])for j in range(self.col)]for i in range(self.row)
            ]
        self.clicked_box = None
        self.draw_grid()

    def draw_grid(self):
        thick_line = 10
        font = pygame.font.SysFont("comicsans", 40)
        dim = self.square_dim / self.boxes_across
        for i in range(self.row):
            for j in range(self.col):
                self.draw_squares(i, j, dim)
                self.draw_grid_lines(i, j, thick_line, dim)
                self.draw_num(i, j, font, dim)

    def draw_num(self, x, y, font, dim):
        if self.game_surface[x][y].num != 0:
            number = font.render(str(self.game_surface[x][y].num), 1, self.WHITE)
            #blit creates a smaller canvas
            self.window.blit(number, ((x*dim) + (dim/2 - number.get_width()/2), (y*dim) + (dim/2 - number.get_height()/2)))
    
    #i = x-axis, j = y-axis
    def draw_grid_lines(self, i, j, thick_line, dim):
        boarder_highlight = self.square_dim / self.boxes_across
        if (i * dim) % boarder_highlight == 0 and i % 3 == 0 and i != 0 and j == 0:
            pygame.draw.line(self.window, self.GREEN, (i*dim, j*dim), (i*dim, self.square_dim), thick_line)
        if (j * dim) % boarder_highlight == 0 and j % 3 == 0 and j != 0 and i == 0:
            pygame.draw.line(self.window, self.GREEN, (i*dim, j*dim), (self.square_dim, j*dim), thick_line)

    """
    Draws the squares onto the pygame window

    @x: x-coord.
    @y: y-coord.
    @dim: pixels across divided by how many sudoku cubes there       are.
    """
    def draw_squares(self, x, y, dim):
        x = x * dim
        y = y * dim
        pygame.draw.rect(self.window, self.GREEN, (x, y, dim, dim), 3) #(surface, (colour), (x, y, width, height), line width)


    def click(self, pos):
        if pos[0] < self.square_dim and pos[1] < self.square_dim:
            dim = self.square_dim / self.boxes_across
            x = pos[0] // dim
            y = pos[1] // dim
            self.clicked_box = (int(x), int(y))
            print("Position:", (x, y))
            return (int(x),int(y))
        else:
            return None
    
    """
    Changes the number at the clicked position of the board.

    @val: The new number for given position on the board.
    """
    def sketch(self, val):
        self.game_surface[self.clicked_box[0]][self.clicked_box[1]].num = val


    """
    Checks to see if the move is valid for the specified move.

    @x: x-coord.
    @y: y-coord.
    @key_press: button pressed by the player.
    """
    def valid(self, x , y, key_press):
        valid_move = False
        pos = self.game_surface[x][y]
        if pos.num == 0:
            for i in range(self.boxes_across): #check x-axis
                if self.game_surface[i][y].num == key_press:
                    return valid_move
            for j in range(self.boxes_across): #check y-axis
                if self.game_surface[x][j].num == key_press:
                    return valid_move
            
            # Check box
            box_x = x // 3
            box_y = y // 3

            for i in range(box_x*3, box_x*3 + 3):
                for j in range(box_y * 3, box_y*3 + 3):
                    if self.game_surface[i][j].num == key_press and (i, j) != (pos.row, pos.col):
                        return valid_move
            
            valid_move = True
            return valid_move
        else:
            return valid_move

    def game_won(self, playing):
        for i in range(self.boxes_across):
            for j in range(self.boxes_across):
                if self.game_surface[i][j].num == 0:
                    return playing
        playing = False
        return playing

    def find_zero(self):
        for i in range(self.boxes_across):
            for j in range(self.boxes_across):
                if self.game_surface[i][j].num == 0:
                    return (i, j)
        return None

    def solve(self):
        empty = self.find_zero()
        if not empty:
            return True
        else:
            row, col = empty

        for i in range(1,10):
                
                if self.valid(row, col, i):
                    self.game_surface[row][col].num = i

                    if self.solve():
                        return True

                    self.game_surface[row][col].num = 0

        return False






            
class Square():
    def __init__(self, row, col, num):
        self.row = row
        self.col = col
        self.num = num



