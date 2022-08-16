"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
action = (None, None)
init_board = board = [[EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY]]
        

def initial_state():
    """
    Returns starting state of the board.
    """
    return init_board


def victor(board): 
    """
    Additional function that checks winner based on the opposite of who's turn it is.
    """    

    if board == init_board:
        return X
    else:
        x_Counter = o_Counter = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    x_Counter += 1
                elif board[i][j] == O:
                    o_Counter += 1
        if x_Counter > o_Counter:
            return X
        else:
            return O


def player(board): #DONE
    """
    Returns player who has the next turn on a board.
    """
    if board == init_board: return X
    else:
        x_Counter = o_Counter = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == X: x_Counter += 1
                elif board[i][j] == O: o_Counter += 1
        if x_Counter <= o_Counter: return X
        else: return O

    raise NotImplementedError


def actions(board): #DONE
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    valid_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                tmp = (i, j)
                valid_moves.add(tmp)
    return valid_moves
    
    raise NotImplementedError


def result(board, action):  #DONE
    """
    Returns the board that results from making move (i, j) on the board.
    Don't change values on `board`, create a tmp for it.
    """

    input = player(board)

    temp_board = copy.deepcopy(board)

    if temp_board[action[0]][action[1]] != EMPTY:
        raise ValueError("Invalid move")
    else:
        temp_board[action[0]][action[1]] = input
    
    return(temp_board)

    raise NotImplementedError


def winner(board): #DONE
    """
    Returns the winner of the game, if there is one.
    """

    #Check for horizontal win
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                break
            elif j == 0:
                current = board[i][j]
                continue
            elif board[i][j] == current and j != 2:
                current = board[i][j]
                continue
            elif board[i][j] != current:
                break
            else:
                return victor(board)

    #Check for vertical win
    for i in range(3):
        for j in range(3):
            if board[j][i] == EMPTY:
                break
            elif j == 0:
                current = board[j][i]
                continue
            elif board[j][i] == current and j != 2:
                current = board[j][i]
                continue
            elif board[j][i] != current:
                break
            else:
                return victor(board)

    #Check for diagonal win
    #left to right
    current = 0

    for i in range(3):
        if i == 0 and board[i][i] != EMPTY:
            current = board[i][i]
            continue
        elif current == board[i][i] and i == 1:
            continue
        elif current == board[i][i] and i == 2:
            return victor(board)
        else:
            break

    #right to left
    for i in reversed(range(3)):
        if i == 2 and board[0][i] != EMPTY:
            current = board[0][i]
            continue
        elif current == board[i][i] and i == 1:
            continue
        elif current == board[2][i] and i == 0:
            return victor(board)
        else:
            break

    return None
    raise NotImplementedError


def terminal(board): #DONE
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
            else:
                continue
    return True
    raise NotImplementedError


def utility(board): #DONE
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) != None:
        w_user = victor(board)
        if w_user == X:
            return 1
        else:
            return -1
    else:
        return 0

    raise NotImplementedError


def minimax(board): #DONE
    """
    Returns the optimal action for the current player on the board.
    """

    def maxValue(board):
        v = -math.inf
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = max(v, minValue(result(board, action)))
        return v

    def minValue(board):
        v = math.inf
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = min(v, maxValue(result(board, action)))
        return v

    if player(board) == X:      #Trying to max score
        v = -math.inf
        bestMove = (None, None)
        for action in actions(board):
            temp = minValue(result(board, action))
            if temp > v:
                v = temp
                bestMove = action

    else:
        v = math.inf
        bestMove = (None, None)
        for action in actions(board):
            temp = maxValue(result(board, action))
            if temp < v:
                v = temp
                bestMove = action
    
    return bestMove
    raise NotImplementedError

