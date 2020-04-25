# TicTacToe game by Tekipeps
# Date Fri Apr 24, 5:47 PM WAT

import random

board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']


# def checkHorizontal():
# def checkVertical():
# def checkForWardDiagonal():
# def checkBackwardDiagonal():

def displayBoard():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])
    print('    ')

def rand():
    arr = []
    for i in range(0, 9):
        if board[i] == ' ':
            arr.append(i)
    return random.choice(arr)

def checkWin():
    if board[0] == board[1] == board[2]:
        return {'win': True, 'player': board[0].upper()}
    elif board[3] == board[4] == board[5]:
        return {'win': True, 'player': board[3].upper()}
    elif board[6] == board[7] == board[8]:
        return {'win': True, 'player': board[6].upper()}
    elif board[0] == board[4] == board[8]:
        return {'win': True, 'player': board[0].upper()}
    elif board[2] == board[4] == board[6]:
        return {'win': True, 'player': board[2].upper()}
    elif board[0] == board[3] == board[6]:
        return {'win': True, 'player': board[0].upper()}
    elif board[1] == board[4] == board[7]:
        return {'win': True, 'player': board[1].upper()}
    elif board[2] == board[5] == board[8]:
        return {'win': True, 'player': board[2].upper()}
    else:
        return {'win': False, 'player': 'tie'}

def move(t):
    if t == 'x':
        while True:
            move = int(input('Your move: ')) - 1
            if board[move] == ' ':
                board[move] = t
                displayBoard()
                break
            else:
                print(f'Position {move} has been occupied enter another move!')
                continue

    elif t == 'o':
        move = rand()
        board[move] = t
        displayBoard()

def restart():
    restart = input('Do you want to restart? Y/n : ')
    if restart.lower() == 'y':
        for i in board:
            board[board.index(i)] = ' '
        game()
    else:
        print('Goodbye!')
        exit()

def game():
    turn = 'x'

    displayBoard()
    for i in range(len(board)):
        # print(turn)
        move(turn)
        if i > 4:
            won = checkWin()
            if won['win'] == True and won['player'] == 'X':
                print('Nice! You won')
                restart()
            elif won['win'] == True and won['player'] == 'O':
                print("Too bad. computer won!")
                restart()
            elif won['win'] == False and i > 8:
                print('Nice try its a tie')
                restart()
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'

if __name__ == "__main__":
    game()
