import os

import pygame as pg

pg.init()

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 400

# SPECIFY THE COLORS OF THE TETRIS BLOCKS
RED = (255,0,0)
GREEN = (0,128,0)
LIGHT_SEA_GREEN = (32,178,170)
MIDNIGHT_BLUE =	(25,25,112)
BLUE_VIOLET = (138,43,226)


def load_game():
    global SCREEN, CLOCK
    SCREEN = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pg.SCALED)
    SCREEN.fill(WHITE)

    while True:
        drawGrid()
        #clock.tick(80)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
               # sys.exit()

        pg.display.update()

def drawGrid():
    gridBlockSize = 40 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, gridBlockSize):
        for y in range(0, WINDOW_HEIGHT, gridBlockSize):
            rect = pg.Rect(x, y, gridBlockSize, gridBlockSize)
            pg.draw.rect(SCREEN, BLACK, rect, 1)
                  
load_game()

def get_blocks():
    # SHAPE FORMATS
    S = [['.....',
        '......',
        '..00..',
        '.00...',
        '.....'],
        ['.....',
        '..0..',
        '..00.',
        '...0.',
        '.....']]

    Z = [['.....',
        '.....',
        '.00..',
        '..00.',
        '.....'],
        ['.....',
        '..0..',
        '.00..',
        '.0...',
        '.....']]

    I = [['..0..',
        '..0..',
        '..0..',
        '..0..',
        '.....'],
        ['.....',
        '0000.',
        '.....',
        '.....',
        '.....']]

    O = [['.....',
        '.....',
        '.00..',
        '.00..',
        '.....']]

    J = [['.....',
        '.0...',
        '.000.',
        '.....',
        '.....'],
        ['.....',
        '..00.',
        '..0..',
        '..0..',
        '.....'],
        ['.....',
        '.....',
        '.000.',
        '...0.',
        '.....'],
        ['.....',
        '..0..',
        '..0..',
        '.00..',
        '.....']]

    L = [['.....',
        '...0.',
        '.000.',
        '.....',
        '.....'],
        ['.....',
        '..0..',
        '..0..',
        '..00.',
        '.....'],
        ['.....',
        '.....',
        '.000.',
        '.0...',
        '.....'],
        ['.....',
        '.00..',
        '..0..',
        '..0..',
        '.....']]

    T = [['.....',
        '..0..',
        '.000.',
        '.....',
        '.....'],
        ['.....',
        '..0..',
        '..00.',
        '..0..',
        '.....'],
        ['.....',
        '.....',
        '.000.',
        '..0..',
        '.....'],
        ['.....',
        '..0..',
        '.00..',
        '..0..',
        '.....']]
        
        
