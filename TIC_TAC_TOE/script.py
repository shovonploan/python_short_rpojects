from os import system as sys


def clear(): return sys('clear')


player1 = None
player2 = None
turns = True
counter = 0
game = 0
pl1p = 0
pl2p = 0
tie = 0
end = True


class Error (Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


class SlotError(Error):
    def __init__(self, message):
        self.message = message


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
                raise InputError('Invalid.\nPlease Enter a correct number.')
        except InputError as e:
            print(e.message)
        except ValueError:
            print('Please Enter a correct NUMBER!')
        else:
            break
    if choose == 2:
        end = False


def display_board(board):
    clear()
    print(f' {board[0]}||{board[1]}||{board[2]}')
    print('---------')
    print(f' {board[3]}||{board[4]}||{board[5]}')
    print('---------')
    print(f' {board[6]}||{board[7]}||{board[8]}')


def player_selection():
    global player1, player2
    print('Choose Your symbol \n \t 1 = X or 2 = O ')
    choose = 0
    while True:
        try:
            choose = int(input())
            if not(choose == 1 or choose == 2):
                raise InputError('Invalid.\nPlease Enter a correct number.')
        except InputError as e:
            print(e.message)
        except ValueError:
            print('Please Enter a correct NUMBER!')
        else:
            break

    if choose == 1:
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'


def handle_turrn(board):
    global player1, player2, turns, counter
    if turns:
        print('\nPlayer 1 Turn')
    else:
        print('\nPlayer 2 Turn')
    print('Select a number from 1-9 \nto place your symbol')
    choose = 0
    while True:
        try:
            choose = int(input())
            if not(choose >= 1 and choose <= 9):
                raise InputError('Invalid.\nPlease Enter a correct number.')
            if (board[choose-1] == 'X' or board[choose-1] == 'O'):
                raise SlotError('Slot is already taken')
        except InputError as e:
            print(e.message)
        except SlotError as e:
            print(e.message)
        except ValueError:
            print('Please Enter a correct NUMBER!')
        else:
            break
    pl = int(choose-1)
    if turns:
        board[pl] = player1
        turns = False
    else:
        board[pl] = player2
        turns = True
    counter = counter+1


def check_rnc(board):
    global player1, player2, pl1p, pl2p
    p = 0
    # for row
    for p in range(3):
        a = 0
        b = 0
        for i in range(p, p+3):
            if board[i] == player1:
                a = a+1
            if board[i] == player2:
                b = b+1
        if a == 3:
            pl1p = pl1p + 1
            return True
        if b == 3:
            pl2p = pl2p + 1
            return True
        p = p+3
    p = 0
    # for clm
    for p in range(3):
        a = 0
        b = 0
        for i in range(p, 9, 3):
            if board[i] == player1:
                a = a+1
            if board[i] == player2:
                b = b+1
        if a == 3:
            pl1p = pl1p + 1
            return True
        if b == 3:
            pl2p = pl2p + 1
            return True
        p = p+1

    return False


def check_dia(board):
    global player1, player2, pl1p, pl2p
    for p in range(1):
        a = 0
        b = 0
        for i in range(0, 9, 4):
            if board[i] == player1:
                a = a+1
            if board[i] == player2:
                b = b+1
        if a == 3:
            pl1p = pl1p + 1
            return True
        if b == 3:
            pl2p = pl2p + 1
            return True

    for p in range(1):
        a = 0
        b = 0
        for i in range(2, 9, 2):
            if (board[i] == player1 and i != 8):
                a = a+1
            if (board[i] == player2 and i != 8):
                b = b+1
        if a == 3:
            pl1p = pl1p + 1
            return True
        if b == 3:
            pl2p = pl2p + 1
            return True
    return False


def game_end(board):
    global counter, tie
    if counter == 9:
        tie = tie+1
        return True
    if check_rnc(board):
        return True
    if check_dia(board):
        return True
    return False


def play_game(board):
    display_board(board)
    while True:
        display_board(board)
        handle_turrn(board)
        display_board(board)
        if game_end(board):
            break


if __name__ == "__main__":
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player_selection()
    while end:
        play_game(board)
        counter = 0
        score_board(board)
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print("Thanks For Playing")
