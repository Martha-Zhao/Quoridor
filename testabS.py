'''
Created on Mar 20, 2019

@author: martha
@ testabS.py
@author: Martha Zhao
@tudo: test if it is possible that depart Minimal function and Maximal function  
'''
from findRoute.gVariables import Board
from findRoute.AStar import findNeighbor,possibleBlockLocation,evaluationFunc
result = None
choice = None
"""
Even node (depth % 2 is  False) is my choice ; owner = 0; Maximal Point;  
        if value > alpha: update alpha; return alpha  
Odd node (depth % 2 is True) is enemy's choice; owner = 1; Minimal Point;
        if value < bet: update beta; return beta
        
moveList = possible piece location and possible block location
        if length(i) == 2: this choice is move piece
        if length(i) == 3: this choice is place block
        if no block placed around piece: moveList = 4 + 40
distance = (enemy's step) - (my step)
            my choice to make distance Max:
            enemy's choice to make distance Minimal
"""
def maxFunc(depth,tempBoard,alpha,beta): #Even node
    myLocation = tempBoard.myPieceLocation
#     enemysLocation = tempBoard.enemysPieceLocation
    if depth <= 0 or tempBoard.isGameOver():
        distance = evaluationFunc(tempBoard)
        return distance
    else:
        moveList = possibleMove(0, tempBoard)
        for i in moveList:
            if len(i) == 2: #move piece
                tempBoard.movePiece(0,myLocation,i)
                val = minFunc(depth - 1,tempBoard,alpha,beta)
                tempBoard.movePiece(0,i,myLocation)
            else:
                tempBoard.placeBlock(0,i[0],i[1],i[2])
                val = minFunc(depth - 1,tempBoard,alpha,beta)
                tempBoard.removeBlock(0,i[0],i[1],i[2])
            if val > alpha:
                alpha = val
                result = val
                choice = i
            if alpha >= beta:
                break
        return alpha
                
def minFunc(depth,tempBoard,alpha,beta):
#     myLocation = tempBoard.myPieceLocation
    enemysLocation = tempBoard.enemysPieceLocation
    if depth <= 0 or tempBoard.isGameOver():
        distance = evaluationFunc(tempBoard)
        return distance
    else:
        moveList = possibleMove(1, tempBoard)
        for i in moveList:
            if len(i) == 2: #move piece
                tempBoard.movePiece(1,enemysLocation,i)
                val = maxFunc(depth - 1,tempBoard,alpha,beta)
                tempBoard.movePiece(1,i,enemysLocation)
            else:
                tempBoard.placeBlock(1,i[0],i[1],i[2])
                val = maxFunc(depth - 1,tempBoard,alpha,beta)
                tempBoard.removeBlock(1,i[0],i[1],i[2])
            if val < beta:
                beta = val
                result = val
                choice = i
            if alpha >= beta:
                break
        return beta    

def possibleMove(owner,tempBoard):
    myPieceLocation = tempBoard.myPieceLocation
    enemysPieceLocation = tempBoard.enemysPieceLocation
    if owner:   #owner = 1 Enemy's choice
        movePieceList = findNeighbor(enemysPieceLocation, tempBoard) 
        moveBlockList = possibleBlockLocation(myPieceLocation, tempBoard)
    else:  #owner = 0 My choice
        movePieceList = findNeighbor(myPieceLocation, tempBoard) 
        moveBlockList = possibleBlockLocation(enemysPieceLocation, tempBoard)
    moveList = movePieceList + moveBlockList
    return moveList  
    
if __name__ == '__main__':
    board = Board((0,3),(6,3))
    print(board.board)
    res = maxFunc(2, board, -0x3f3f3f, 0x3f3f3f)
    print('choice is ' + repr(choice) + ' res is '+ repr(res))
