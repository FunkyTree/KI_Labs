import random
import game
<<<<<<< HEAD
import math
import sys
=======
import sys
import time
>>>>>>> 510ae3ec61ccfc7d4abb73744119d89f5f4ad5a0
import numpy as np

# Author:				chrn (original by nneonneo)
# Date:				11.11.2016
# Description:			The logic of the AI to beat the game.

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

def find_best_move(board):
<<<<<<< HEAD
    bestmove = -1    
	
    moves = [game.merge_up, game.merge_down, game.merge_left, game.merge_right]
        
    goal = []
    for i in range(4):
        goal.append([2**((i*4)+j+1) for j in range(4)])
    
    blocks = sum(sum(x > 0 for x in board))
        
    goal[1] = goal[1][::-1]
    
    # if (isOptimalMergeLeft(board, 3) < 0):
        # goal[2] = goal[2][::-1]
    # if (blocks > 8 & ~isOptimalMergeLeft(board, 2) < 0):
        # goal[1] = goal[1][::-1]
    # if (blocks > 12 & isOptimalMergeLeft(board, 1) < 0):
        # goal[0] = goal[0][::-1]
    
    if (blocks > 12):
        goal[2] = goal[2][::-1]
    if (blocks > 13):
        goal[0] = goal[0][::-1]
    if (blocks > 14):    
        goal[1] = goal[1][::-1]
    
    nextTurn = []
    for i in range(4):
        nextTurn.append(moves[i](board))
    
    sums = []
    for i in range(4):
        sums.append(sum(sum([x*y for x,y in zip(goal, nextTurn[i])])))
    
    maxi = max(sums)
    bestmove = sums.index(maxi)
    
    while (areListsEqual(board, moves[bestmove](board))):
        sums[bestmove] = 0
        if(bestmove == 1):
            sums[0] = 0
        maxi = max(sums)
        bestmove = sums.index(maxi)
    
    return bestmove

def getBlocks(board, move):
    return sum(sum(x > 0 for x in move(board)))
    
def getMaxMergeMove(board):
    merges = [game.merge_up(board), game.merge_down(board), game.merge_left(board), game.merge_right(board)]
    blocks = sum(sum(x > 0 for x in merges))
    return blocks.tolist().index(min(blocks));
    
def isOptimalMergeLeft(board, row):
    rateOrientation = 0;
    rateMinimum = 1000;
    for i in range(4):
        difs = []
        block = board[row][i]
        for j in range(4):
            difs.append(block - board[row-1][j])
        
        mindif = min(difs)
        index = difs.index(mindif)
        if (sum(i == mindif for i in difs) > 1):
            t = difs[::-1]
            index = 3 - t.index(mindif)
        rate = []
        
        block2 = board[row-1][index]
        
        # calc log
        blockLog = 0
        if (block > 0):
            blockLog = math.log(block, 2)
        block2Log = 0
        if (block2 > 0):
            block2Log = math.log(block2, 2) 
        rate.append(abs(blockLog - block2Log))
        minrate = min(rate)
        
        if (minrate < rateMinimum):
            rateOrientation = rate.index(minrate) - i
            rateMinimum = minrate
    return rateOrientation
    
def areListsEqual(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if (a[i][j] != b[i][j]):
=======
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
>>>>>>> 510ae3ec61ccfc7d4abb73744119d89f5f4ad5a0
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