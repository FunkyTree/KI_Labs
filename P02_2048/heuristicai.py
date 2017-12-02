import random
import game
import sys
import time
import numpy as np

# Author:				chrn (original by nneonneo)
# Date:				11.11.2016
# Description:			The logic of the AI to beat the game.

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

def find_best_move(board):
    bestmove = -1
	
    moves = [game.merge_up, game.merge_down, game.merge_left, game.merge_right]
	
    goal = []
    if (sum(sum(board)) % 20 < 2):
        for i in range(0,4):
            goal.append([2**((4*i)+j+1) for j in range(0,4)])
    
        goal[3] = goal[3][::-1]
        goal[1] = goal[1][::-1]
    else:
        for i in range(4):
            goal.append([2**(i+j) for j in range(4)])
    
	
    u = game.merge_up(board)
    d = game.merge_down(board)
    r = game.merge_right(board)
    l = game.merge_left(board)
	
    U = [x * y for x,y in zip(goal, u)]
    D = [x * y for x,y in zip(goal, d)]
    R = [x * y for x,y in zip(goal, r)]
    L = [x * y for x,y in zip(goal, l)]
    
    sumU = sum(sum(U))
    sumD = sum(sum(D))
    sumR = sum(sum(R))
    sumL = sum(sum(L))
	    
    sums = [sumU, sumD, sumL, sumR]
    best = max(sums)
    bestmove = sums.index(best)    
    
    while (areEqual(board, moves[bestmove](board))):
        sums[bestmove] = 0
        best = max(sums)
        bestmove = sums.index(best)
	
    return bestmove

def areEqual(a, b):
    for x in range(len(a)):
        for y in range(len(a[x])):
            if (a[x][y] != b[x][y]):
                return False
    return True

def find_best_move_random_agent():
    return random.choice([UP,DOWN,LEFT,RIGHT])
    
def execute_move(move, board):
    """
    move and return the grid without a new random tile 
	It won't affect the state of the game in the browser.
    """

    if move == UP:
        return game.merge_up(board)
    elif move == DOWN:
        return game.merge_down(board)
    elif move == LEFT:
        return game.merge_left(board)
    elif move == RIGHT:
        return game.merge_right(board)
    else:
        sys.exit("No valid move")
		
def board_equals(board, newboard):
    """
    Check if two boards are equal
    """
    return  (newboard == board).all()  