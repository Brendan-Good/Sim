#!/usr/bin/env python3

#Negamax implementation by Joshua Brule

from collections import deque
from copy import deepcopy

N = 7 #width
M = 6 #height
MAX_DEPTH = 4

inf = float('inf')
    
def negamax(node, depth, alpha, beta, player):
    '''Perform a depth limited negamax search using functions eval(), expand()
    and isTerminal() as appropriate
    
    Returns (optimal move, negamax value)
    
    Usage: negamax(new_board(), MAX_DEPTH, -inf, +inf, 1)'''
    
    if depth == 0 or is_terminal(node):
        return (None, player * eval(node))
    else:
        candidate_move = None
        for move in expand(node, player):
            val = -1 * negamax(move, depth - 1, -beta, -alpha, -player)[1]
            if val >= beta:
                return (None, val)
            if val > alpha:
                candidate_move = move
                alpha = val
                
        return (candidate_move, alpha)
        
def expand(node, player):
    '''Expands node for player'''
    moves = []
    
    for i in range(0, N):
        new_node = deepcopy(node)
        for j in range(0, M):
            if new_node[i][j] == 0:
                new_node[i][j] = player
                moves.append(new_node)
                break
            
    return moves
    
def is_terminal(node):
    '''Returns true iff node is a terminal position'''
    
    #check for a win (naive)
    for i in range(0, N):
        for j in range(0, M):
            if (col_win(node, i, j) or row_win(node, i, j) or
                slash_win(node, i, j) or backslash_win(node, i, j)):
                return True
    
    #return false if there are still open spaces
    for i in range(0, N):
        for j in range(0, M):
            if not (node[i][j] == -1 or node[i][j] == 1):
                return False
        
    #fall-through (board is drawn)
    return True
    
def col_win(node, i, j):
    '''Returns node[i][j] iff the col starting at (i,j) is 4 identical pieces
    0 otherwise'''
    if j > (M - 4):
        return 0
        
    if (node[i][j] == node[i][j + 1] == node[i][j + 2] ==
            node[i][j + 3]):
        return node[i][j]
    else:
        return 0

def row_win(node, i, j):
    '''Returns node[i][j] iff the row ...'''
    if i > (N - 4):
        return 0
        
    if (node[i][j] == node[i + 1][j] == node[i + 2][j] ==
            node[i + 3][j]):
        return node[i][j]
    else:
        return 0

def slash_win(node, i, j):
    '''Returns node[i][j] iff the slash ...'''
    if i > (N - 4) or j > (M - 4):
        return 0
        
    if (node[i][j] == node[i + 1][j + 1] == node[i + 2][j + 2] ==
            node[i + 3][j + 3]):
        return node[i][j]
    else:
        return 0
        
def backslash_win(node, i, j):
    '''Returns node[i][j] iff the backslash ...'''
    if i > (N - 4) or j < 3:
        return 0
        
    if (node[i][j] == node[i + 1][j - 1] == node[i + 2][j - 2] ==
            node[i + 3][j - 3]):
        return node[i][j]
    else:
        return 0
    
def eval(node):
    '''Returns the static evaluation of node
    
    This is a very naive implementation that assigns every square a value
    based on its surrounding (up, left, diag up, diag down) squares
    '''
    val = 0
    for i in range(0, N):
        for j in range(0, M):
            val += point_val(node, i, j)
    
    return val
    
def point_val(node, i, j):
    '''Static value of the (i, j) point
    
    Naive implementation
    '''
    val = 0
    
    line2 = 10 #every 2 in a line gets 10 points
    line3 = 30 #3 in a line gets an additional 30 points
    
    if node[i][j] == 0:
        return 0
    
    #make node bigger to avoid bounds checks
    enode = deepcopy(node)
    for col in enode:
        col.extend([0,0,0])
    enode.extend([[0 for i in range(M+3)] for j in range(3)])
    
    #3 in a line
    if enode[i][j] == enode[i][j+1] == enode[i][j+2]:
        val += line3 * enode[i][j]
    if enode[i][j] == enode[i+1][j+1] == enode[i+2][j+2]:
        val += line3 * enode[i][j]
    if enode[i][j] == enode[i+1][j-1] == enode[i+2][j-2]:
        val += line3 * enode[i][j]
    if enode[i][j] == enode[i+1][j] == enode[i+2][j]:
        val += line3 * enode[i][j]
    
    #2 in a line
    if enode[i][j] == enode[i][j+1]:
        val += line2 * enode[i][j]
    if enode[i][j] == enode[i+1][j+1]:
        val += line2 * enode[i][j]
    if enode[i][j] == enode[i+1][j-1]:
        val += line2 * enode[i][j]
    if enode[i][j] == enode[i+1][j]:
        val += line2 * enode[i][j]
        
    #win is worth inf, loss is worth -inf
    winner = (col_win(node, i, j) + row_win(node, i, j) +
              slash_win(node, i, j) + backslash_win(node, i, j))
    if winner != 0:
        val = inf * winner
        
    return val
    
def new_board():
    '''Generate an empty NxM board'''
    x = list()
    for i in range(0, N):
        x.append(list())
        for j in range(0, M):
            x[i].append(0)
    
    return x
    
def sign_str(val):
    '''Equivalent to str(sign(float_value))'''
    if val > 0:
        return "+"
    elif val < 0:
        return "-"
    else:
        return " "

        
def print_board(board):
    '''Pretty-print the board'''
    if board == None:
        print("GAME OVER")
        return None
    
    for j in range(M):
        for i in range(N):
            print(sign_str(board[i][M - j - 1]), end='')
            
        print()
        
    for i in range(N):
        print("=", end='')
        
    print()
    return None

#play a short game
board = new_board()
for i in range(0, N*M + 1):
    board = negamax(board, MAX_DEPTH, -inf, +inf, (((i + 1) % 2) * 2 - 1))[0]
    print_board(board)
    if board == None:
        break
