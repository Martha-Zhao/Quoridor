"""
@ alphaBetaCut.py
@author: Martha Zhao
@todo: cut decision with alpha-beta cut
        first in minmax cut  
        test minMax function failed
"""

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
def alphaBetaSerch(depth,tempBoard,alpha,beta):
    myLocation = tempBoard.myPieceLocation
    enemyLocation = tempBoard.enemysPieceLocation
    if depth<=0 or tempBoard.isGameOver():
        """
        change owner with depth
        """
        distance = evaluationFunc(tempBoard)
        return distance
    else:
        moveList = possibleMove(myLocation,enemyLocation,tempBoard)
        for i in moveList:
            """
            make next move
            """
            if len(i) == 2: #move Piece
                tempBoard.movePiece(myLocation,i)
            else:
                tempBoard.placeBlock(i[0],i[1],i[2])
                
            val = alphaBetaSerch(depth - 1, tempBoard, alpha, beta)
            if (not depth % 2) and val > alpha: #Even---Max---update Alpha
                alpha = val
                result = val
                choice = i
            elif depth % 2 and val < beta:#Odd---Min---update Beta
                beta = val
                result = val
                choice = i
            if alpha >= beta:
                break
        if depth%2:
            return beta
        else:
            return alpha  
        
def possibleMove(myPieceLocation,enemyPieceLocation,tempBoard):
    movePieceList = findNeighbor(myPieceLocation, tempBoard) 
    moveBlockList = possibleBlockLocation(enemyPieceLocation, tempBoard)
    moveList = movePieceList + moveBlockList
    return moveList  

              
if __name__ == '__main__':
    board = Board((0,3),(6,3))
    print(board.board)
    res = alphaBetaSerch(2, board, -0x3f3f3f, 0x3f3f3f)
    print(res)
