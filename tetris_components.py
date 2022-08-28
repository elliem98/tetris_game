import os

import pygame as pg

pg.init()

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 400

def load_game():
    global SCREEN, CLOCK
    SCREEN = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pg.SCALED)
    SCREEN.fill(WHITE)

    while True:
        drawGrid()
        #clock.tick(60)
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

    
    
