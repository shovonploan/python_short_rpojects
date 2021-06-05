import numpy as np
import pygame
import sys
import math

board = np.zeros((6, 7))
turn = 0
game = 0
pl1p = 0
pl2p = 0
tie = 0
end = False
win = None


class Error (Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


class SlotError(Error):
    def __init__(self, message):
        self.message = message

def er1(choose, num):
    for i in range(1, num+1):
        if choose == i:
            return True
    return False


def process(num, board,col):
    num += 1
    choose = 0
    while True:
        try:
            choose = col
            if not(er1(choose, num)):
                raise InputError('Invalid.\nPlease Enter a correct number.')
            elif (choose == 8):
                raise InputError('Invalid.\nPlease Enter a correct number.')
            elif (choose == 7):
                choose = 0
            elif not(board[0,choose] == np.zeros((1))):
                raise SlotError('Column is not empty')
        except InputError as e:
            print(e.message)
        except SlotError as e:
            print(e.message)
        except ValueError:
            print('Please Enter a correct NUMBER!')
        else:
            break
    return choose-1


def score_board(board):
    display_board(board)
    global pl1p, pl2p, end, game, tie
    print(
        f'Total Number of game:{game}\nPlayer 1 won:{pl1p}\nPlayer 2 won:{pl2p}\n Numer of tie:{tie}')
    choose = 0
    print('Wanna play more?\n1=Yes\t2=No')
    while True:
        try:
            choose = int(input())
            if not(choose == 1 or choose == 2):
                raise Error.InputError(
                    'Invalid.\nPlease Enter a correct number.')
        except Error.InputError as e:
            print(e.message)
        except ValueError:
            print('Please Enter a correct NUMBER!')
        else:
            break
    if choose == 2:
        end = True


def display_board(b):
    print(b)

def drop_peace(selection, board, turn):
    row = 0
    turn+=1
    for i in range(6):
        if not(np.allclose(board[i][selection],np.zeros((1)))):
            break
        row = i
    board[row,selection] = turn


def handle_turrn(board,col):
    global turn
    if turn == 0:
        print("Player 1 Make Your Selection (1-7)")
        selection = process(7, board,col)
        turn = 1
        drop_peace(selection, board, turn)

    else:
        print("Player 2 Make Your Selection (1-7)")
        selection = process(7, board,col)
        turn = 0
        drop_peace(selection, board, turn)

def win_or_tie(board):
    global win
    for r in range(5,-1,-1):
        for c in range(4):
            if board[r][c] == 2 and board[r][c+1] == 2 and board[r][c+2] == 2 and board[r][c+3] == 2: 
                win = 1
                return True
            if board[r][c] == 1 and board[r][c+1] == 1 and board[r][c+2] == 1 and board[r][c+3] == 1: 
                win = 2
                return True
        for c in range(6,2,-1):
            if board[r][c] == 2 and board[r][c-1] == 2 and board[r][c-2] == 2 and board[r][c-3] == 2: 
                win = 1
                return True
            if board[r][c] == 1 and board[r][c-1] == 1 and board[r][c-2] == 1 and board[r][c-3] == 1: 
                win = 2
                return True
    for c in range(7):
        for r in range(3):
            if board[r][c] == 2 and board[r+1][c] == 2 and board[r+2][c] == 2 and board[r+3][c] == 2: 
                win = 1
                return True
            if board[r][c] == 1 and board[r+1][c] == 1 and board[r+2][c] == 1 and board[r+3][c]== 1: 
                win = 2
                return True
        for r in range(5,2,-1):
            if board[r][c] == 2 and board[r-1][c] == 2 and board[r-2][c] == 2 and board[r-3][c] == 2: 
                win = 1
                return True
            if board[r][c] == 1 and board[r-1][c] == 1 and board[r-2][c] == 1 and board[r-3][c] == 1: 
                win = 2
                return True
    for r in range(3,6):
        for c in range(0,4):
            if board[r][c]==2 and board[r-1][c+1]==2 and board[r-2][c+2] == 2 and  board[r-3][c+3]==2:
                win = 1
                return True
            if board[r][c]==1 and board[r-1][c+1]==1 and board[r-2][c+2] == 1 and  board[r-3][c+3]==1:
                win = 2
                return True
    return False

def draw_board(board):
	for c in range(7):
		for r in range(6):
			pygame.draw.rect(screen,(0,0,255), (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, (0,0,0), (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(7):
		for r in range(6):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, (255,0,0), (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, (255,255,0), (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()

pygame.init()
SQUARESIZE = 100
width = 7 * SQUARESIZE
height = (6+1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monspace", 75)
def play_game():
    global win, board
    win = None
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.Quit:
                sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                handle_turrn(board,col)
                if win_or_tie(board):
                    game_over = True
                    score_board(board)



if __name__ == "__main__":
    draw_board(board)
    pygame.display.update
    play_game()

