"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xNum = 0
    oNum = 0

    for row in board:
        xNum += row.count(X)
        oNum += row.count(O)

    if xNum <= oNum:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()

    for indexR, row in enumerate(board):
        for indexC, item in enumerate(row):
            if item == None:
                possible_moves.add((indexR, indexC))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    playerMove = player(board)

    newState = deepcopy(board)

    i, j = action

    if board[i][j] != None:
        raise Exception
    else:
        newState[i][j] = playerMove

    return newState


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in (X, O):
        for row in board:
            if row == [player] * 3:
                return player

        for i in range(3):
            column = [board[x][i] for x in range(3)]
            if column == [player] * 3:
                return player

        if [board[i][i] for i in range (0, 3)] == [player] * 3:
            return player

        elif [board[i][~i] for i in range(0, 3)] == [player] * 3:
            return player
    return None
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True


    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def MAX_VALUE(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -9999
            for action in actions(board):
                MINVAL = MIN_VALUE(result(board, action)) [0]
                if MINVAL > v:
                    v = MINVAL
                    optimal_move = action
            return v, optimal_move

    def MIN_VALUE(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = 9999
            for action in actions(board):
                MAXVAL = MAX_VALUE(result(board,action)) [0]
                if MAXVAL < v:
                    v = MAXVAL
                    optimal_move = action
            return v, optimal_move

    currPlayer = player(board)

    if terminal(board):
        return None

    if currPlayer == X:
        return MAX_VALUE(board)[1]
    else:
        return MIN_VALUE(board)[1]
