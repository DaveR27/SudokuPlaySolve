import Game
import VideoDriver
import os

def main():
    VideoDriver.setup_video()
    sudoku = Game.Game()
    sudoku.run_game()

if __name__ == "__main__":
    main()