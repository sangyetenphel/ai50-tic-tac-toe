"""
Tic Tac Toe Player
"""

import math
import copy
import numpy

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
    xs  = 0
    os = 0
    for players in board:
        xs += players.count(X)
        os += players.count(O)

    if xs == os:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for row, cell in enumerate(board):
        for cell_idx, player in enumerate(cell):
            if player == EMPTY:
                possible_actions.add((row, cell_idx))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    i, j = action

    # making a deep copy of the board in hand
    new_board = copy.deepcopy(board)

    if new_board[i][j] is not EMPTY:
        raise Exception("Invalid move")
    else:
        new_board[i][j] = turn

    return new_board  


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # checking if any horizontal rows match
    for rows in board:
        if rows.count(X) == 3 or rows.count(O) == 3:
            return rows[0]

    # for vertical matches
    vertical = numpy.transpose(board).tolist()

    for rows in vertical:
        if rows.count(X) == 3 or rows.count(O) == 3:
            return rows[0]
    
    # for diagonal matches
    if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
        return board[0][0]
    if (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]):
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True
    
    for cell in board:
        if EMPTY in cell:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)
    if won == X:
        return 1
    elif won == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    optimal_action = None
    
    highest_value = -9999
    lowest_value = 9999
    alpha = -9999
    beta = 9999
    
    if current_player == X:
        for action in actions(board):
            current_highest = min_value(result(board, action),alpha, beta) 
            if current_highest > highest_value:
                highest_value = current_highest
                optimal_action = action
            alpha = highest_value


    if current_player == O:
        for action in actions(board):
            current_lowest = max_value(result(board, action), alpha, beta) 
            if current_lowest < lowest_value:
                lowest_value = current_lowest
                optimal_action = action
            beta = lowest_value

    return optimal_action


def max_value(board, alpha, beta):
    """
    Return the max possible value from a given state
    """
    if terminal(board):
        return utility(board)
    
    v = -9999
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        if v < alpha:
            break
    return v

def min_value(board, alpha, beta):
    """
    Return the max possible value from a given state
    """
    if terminal(board):
        return utility(board)
    
    v = 9999
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        if v > beta:
            break
    return v


"""
Tic Tac Toe Player
"""

import math
import copy
import numpy

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
    xs  = 0
    os = 0
    for players in board:
        xs += players.count(X)
        os += players.count(O)

    if xs == os:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for row, cell in enumerate(board):
        for cell_idx, player in enumerate(cell):
            if player == EMPTY:
                possible_actions.add((row, cell_idx))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    i, j = action

    # making a deep copy of the board in hand
    new_board = copy.deepcopy(board)

    if new_board[i][j] is not EMPTY:
        raise Exception("Invalid move")
    else:
        new_board[i][j] = turn

    return new_board  


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # checking if any horizontal rows match
    for rows in board:
        if rows.count(X) == 3 or rows.count(O) == 3:
            return rows[0]

    # for vertical matches
    vertical = numpy.transpose(board).tolist()

    for rows in vertical:
        if rows.count(X) == 3 or rows.count(O) == 3:
            return rows[0]
    
    # for diagonal matches
    if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
        return board[0][0]
    if (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]):
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True
    
    for cell in board:
        if EMPTY in cell:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)
    if won == X:
        return 1
    elif won == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    optimal_action = None
    
    alpha = -9999
    beta = 9999
    
    if current_player == X:
        for action in actions(board):
            current_highest = min_value(result(board, action), alpha, beta) 
            if current_highest > alpha:
                alpha = current_highest
                optimal_action = action


    if current_player == O:
        for action in actions(board):
            current_lowest = max_value(result(board, action), alpha, beta) 
            if current_lowest < beta:
                beta = current_lowest
                optimal_action = action

    return optimal_action


def max_value(board, alpha, beta):
    """
    Return the max possible value from a given state
    """
    if terminal(board):
        return utility(board)
    
    v = -9999
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        if v < alpha:
            break
    return v


def min_value(board, alpha, beta):
    """
    Return the max possible value from a given state
    """
    if terminal(board):
        return utility(board)
    
    v = 9999
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        if v > beta:
            break
    return v


