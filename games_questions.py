from random import randint

class Stack:
    def __init__(self):
        self._list = []
    
    def __len__(self):
        return len(self._list)    
    
    def push(self, element):
        if len(self._list) <= 6:
            self._list.append(element)
        else:
            return
    
    def peek(self):
        return self._list[-1]

def initBoard():
    rows = ['a','b','c','d','e','f']
    board = []
    for i in range(0,len(rows)):
        board.append([' '] * 7)
    
    return board


def initStacks():
    S = [ Stack(), Stack(), Stack(), 
         Stack(), Stack(), Stack(), Stack() ]
    return S


def printBoard(board):
    rows = ['a','b','c','d','e','f']
    top = '    1   2   3   4   5   6   7   '
    row = [[n] for n in range(0,7)]
    row[0][0] = 'f | '
    row[1][0] = 'e | '
    row[2][0] = 'd | '
    row[3][0] = 'c | '
    row[4][0] = 'b | '
    row[5][0] = 'a | '
    print('')
    print('  ' + '-'*(len(top)-3))
    for j in range(0,len(rows)):
        for i in range(1,8):
            row[j][0] = row[j][0] + str(board[j][i-1]) + ' | '
        print(row[j][0])
        print('  ' + '-'*((len(row[j][0])-3)))
    print(top)
    print('')
    


def move(piece, board, Stacks, computer):
    Set0 = {'1','2','3','4','5','6','7'}
    if piece == computer:
        pos = randint(1,7)
        if len(Stacks[pos-1]) < 6:
            Stacks[pos-1].push(piece)
            board[6-len(Stacks[pos-1])][pos-1] = \
                Stacks[pos-1].peek()
        else:
            move(piece, board, Stacks, computer)
    else:
        pos = str(input('Your move: '))
        if (pos in Set0) == False:
            print('Input must be integer between 1 and 7')
            move(piece, board, Stacks, computer)
        else: 
            pos = int(pos)
            if len(Stacks[pos-1]) < 6:
                Stacks[pos-1].push(piece)
                board[6-len(Stacks[pos-1])][pos-1] = \
                    Stacks[pos-1].peek()
            else:
                print('Column full, try again...')
                move(piece, board, Stacks, computer)
    return board, Stacks


def checkWin(S,board):
    game = False   
    # Check for horizontal win
    for j in range(0,6):
        for i in range(3,7):
            if (board[j][i]==board[j][i-1]==\
                board[j][i-2]==board[j][i-3]==S):
                    game = True
            else:
                continue   
    # Check for vertical win
    for i in range(0,7):
        for j in range(3,6):
            if (board[j][i]==board[j-1][i]==\
                board[j-2][i]==board[j-3][i]==S):
                    game = True
            else:
                continue
    # Check for diagonal win
    for i in range(0,4):
        for j in range(0,3):
            if (board[j][i]==board[j+1][i+1]==\
                board[j+2][i+2]==board[j+3][i+3]==S or
                board[j+3][i]==board[j+2][i+1]==\
                board[j+1][i+2]==board[j][i+3]==S):
                    game = True
            else:
                continue
    if game == True:
        print(S + ' wins!')
    return game


def main():
    player1 = str( input('Choose X or O: ') )
    if player1 != 'X' and player1 != 'O':
        player1 = str( input('Choose X or O: ') )
    if player1 == 'X':
        computer1 = 'O'
    else:
        computer1 = 'X'
        
    # Print board
    board = initBoard()
    Stacks = initStacks()
    printBoard(board)
    print('Enter an integer between 1 to 7 ')
    game = False
    while game == False:
        # X player
        board, Stacks = move('X',board,Stacks,computer1)
        printBoard(board)
        game = checkWin('X',board)
        if game == True:
            break
# O player
        board, Stacks = move('O',board,Stacks,computer1)
        printBoard(board)
        game = checkWin('O',board)
        if game == True:
            break
    print('Good game.')
if __name__ == '__main__':
    main()