from inspect import _Object
import os
import random
import pygame as pg

pg.init()
pg.font.init()

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 400
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1200

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

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0,128,0), (255, 0, 0), (32,178,170), (25,25,112), (255, 165, 0), (138,43,226), (128, 0, 128)]
        

class Piece(Object):
    rows = 20 #y coord
    columns = 10 # x coord

    # create special method for instance of pieces/shapes where each shape has a color and coordinates in grid 
    def __init__(self, column, row, shape):
            self.x = column
            self.y = row
            self.shape = shape
            self.color =  shape_colors[shapes.index(shape)]
            self.rotation = 0 # specifies the starting number to rotate with, the range is from 0 to 3 rotations

