'''
Created on 2019年3月22日

@author: Martha Zhao
'''
# from findRoute.gVariables import Board
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
choice:
        if depth is even first use Max function result is best for my step
        if change side SHOULD 
        COMMAND SENTENCE : choice = i  IN maxfunc 
        AND UNCOMMAND SENTENCE choice = i IN minFunc 
"""
def maxFunc(depth,tempBoard,alpha,beta): #Even node
    global choice
    myLocation = tempBoard.myPieceLocation
#     enemysLocation = tempBoard.enemysPieceLocation
    if depth <= 0 or tempBoard.isGameOver(): #find end node ,calculate and return distance
        distance = evaluationFunc(tempBoard)
        return distance
    else:
        moveList = possibleMove(0, tempBoard) #find possible moves
        for i in moveList:
            if len(i) == 2: #move piece
                tempBoard.movePiece(0,i)
                val = minFunc(depth - 1,tempBoard,alpha,beta)
                tempBoard.movePiece(0,myLocation) #reset board
            else: #place block
                tempBoard.placeBlock(0,i[0],i[1],i[2])
                val = minFunc(depth - 1,tempBoard,alpha,beta)
                tempBoard.removeBlock(0,i[0],i[1],i[2]) #reset board
            if val > alpha: #if has better option change change and result
                alpha = val
                result = val
                choice = i
            if alpha >= beta: #if no better option available end search
                break
        return alpha 
                
def minFunc(depth,tempBoard,alpha,beta): #Odd node
    global choice
#     myLocation = tempBoard.myPieceLocation
    enemysLocation = tempBoard.enemysPieceLocation 
    #find end node ,calculate and return distance
    if depth <= 0 or tempBoard.isGameOver(): 
        distance = evaluationFunc(tempBoard)
        return distance
    else:
        moveList = possibleMove(1, tempBoard)
        for i in moveList:
            if len(i) == 2: #move piece
                tempBoard.movePiece(1,i)
                val = maxFunc(depth - 1,tempBoard,alpha,beta)
                tempBoard.movePiece(1,enemysLocation)
            else:
                tempBoard.placeBlock(1,i[0],i[1],i[2])
                val = maxFunc(depth - 1,tempBoard,alpha,beta)
                tempBoard.removeBlock(1,i[0],i[1],i[2])
            if val < beta:
                beta = val
                result = val
#                 choice = i
            if alpha >= beta:
                break
        return beta    

def possibleMove(owner,tempBoard):
    myPieceLocation = tempBoard.myPieceLocation
    enemysPieceLocation = tempBoard.enemysPieceLocation
    if owner:   #owner = 1 Enemy's choice
        movePieceList = findNeighbor(1,enemysPieceLocation, tempBoard) 
        moveBlockList = possibleBlockLocation(myPieceLocation, tempBoard)
    else:  #owner = 0 My choice
        movePieceList = findNeighbor(0,myPieceLocation, tempBoard) 
        moveBlockList = possibleBlockLocation(enemysPieceLocation, tempBoard)
    moveList = movePieceList + moveBlockList
#     moveList = movePieceList
    return moveList  

"""
function IN 
"""
def abS(depth,tempBoard):
    global choice
    alpha = -0x3f3f3f
    beta = 0x3f3f3f
    if depth%2:
        res = minFunc(depth, tempBoard, alpha, beta)
    else:
        res = maxFunc(depth, tempBoard, alpha, beta)
    print('alphaBeta pruning result = ',res)
    return (choice)