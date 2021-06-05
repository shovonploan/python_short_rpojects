import numpy as np
import pygame 
import sys

# BLUE = (0,0,255)
# BLACK = (0,0,0)
# RED = (255,0,0)
# YELLOW = (255,255,0)

# ROW_COUNT = 6
# COLUMN_COUNT = 12

board = np.zeros((6,7))

def draw_board(board):
    for c in range(7):
        for r in range(6):
            pygame.draw.rect(screen,(0,0,255), (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE,SQUARESIZE,SQUARESIZE ))

pygame.init()

SQUARESIZE = 100
width = 7 * SQUARESIZE
height = 6 * SQUARESIZE

size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update

while not True:
        for event in pygame.event.get():
            if event.type == pygame.Quit:
                sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass