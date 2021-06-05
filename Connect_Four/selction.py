from numpy import zeros as z

class Error (Exception):
    pass
class InputError(Error):
    def __init__(self,message):
        self.message=message
class SlotError(Error):
    def __init__(self,message):
        self.message=message

def er1(choose,num):
    for i in range(1,num):
        if choose == i:
            return True
    return False

def process(num,board):
    num +=1
    choose = 0
    while True:
        try:
            choose = int(input())
            if not(er1(choose,num)):
                raise InputError(
                    'Invalid.\nPlease Enter a correct number.')
            if not(board[0][0]==z((1))):
                raise SlotError('Column is not empty')
        except InputError as e:
            print(e.message)
        except SlotError as e:
            print(e.message)
        except ValueError:
            print('Please Enter a correct NUMBER!')
        else:
            break
