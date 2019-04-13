'''
Unbeatable Tic-Tac-Toe
using Minimax + Alpha-Beta pruning
Author: https://github.com/nisaruj
'''


class style():
    def BLACK(x): return '\033[30m' + str(x)
    def RED(x): return '\033[31m' + str(x)
    def GREEN(x): return '\033[32m' + str(x)
    def YELLOW(x): return '\033[33m' + str(x)
    def BLUE(x): return '\033[34m' + str(x)
    def MAGENTA(x): return '\033[35m' + str(x)
    def CYAN(x): return '\033[36m' + str(x)
    def WHITE(x): return '\033[37m' + str(x)
    def UNDERLINE(x): return '\033[4m' + str(x)
    def RESET(x): return '\033[0m' + str(x)


def printBoard(board):
    print(style.RESET(''), end='')
    print('-'*13)
    for i in range(3):
        print(style.RESET('| '), end='')
        print(style.RESET(' | ').join([style.YELLOW(
            str(j)) if board[j] == '' else board[j] for j in range(i*3, 3*(i+1))]), end='')
        print(style.RESET(' |'))
        print('-'*13)


def gameOver(board):
    if board.count('') == 0:
        return (True, 0)
    winIndex = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for (a, b, c) in winIndex:
        if board[a] == board[b] == board[c] and board[a] != '':
            return (True, 1 if board[a] == 'O' else -1)
    return (False, 0)


def minimax(board, depth, alpha, beta, isMaxPlayer):
    isGameOver = gameOver(board)
    if depth == 0 or isGameOver[0] != False:
        return {'value': isGameOver[1], 'action': -1}

    if isMaxPlayer:
        value = -float('Inf')
        action = -1
        for i in range(9):
            if board[i] == '':
                newBoard = list(board)
                newBoard[i] = 'O'
                miniMax = minimax(newBoard, alpha, beta,
                                  depth - 1, False)['value']
                if value < miniMax:
                    value = miniMax
                    action = i
                alpha = max(value, alpha)
                if alpha >= beta:
                    break
    else:
        value = float('Inf')
        action = -1
        for i in range(9):
            if board[i] == '':
                newBoard = list(board)
                newBoard[i] = 'X'
                miniMax = minimax(newBoard, alpha, beta,
                                  depth - 1, True)['value']
                if value > miniMax:
                    value = miniMax
                    action = i
                beta = min(value, beta)
                if alpha >= beta:
                    break

    return {'value': value, 'action': action}


def main():
    board = [''] * 9
    while True:
        printBoard(board)
        isGameOver = gameOver(board)
        if isGameOver[0]:
            print({
                1: style.RED('You Lose!'),
                0: style.CYAN('Draw!'),
                -1: style.GREEN('You Win!')
            }[isGameOver[1]])
            print(style.RESET('Exiting ...'))
            exit()
        index = int(input("Choose position to place X: "))
        if board[index] != '':
            continue
        board[index] = 'X'
        board[minimax(board, 1000, -float('Inf'),
                      float('Inf'), True)['action']] = 'O'


if __name__ == "__main__":
    main()