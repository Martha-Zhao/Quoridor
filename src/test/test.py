'''
Created on 2019年3月22日

@author: Martha Zhao
@todo: all the test available
'''

# from cheseBoard.preBoard import 
from findRoute.AStar import findNeighbor,possibleBlockLocation,AStar
from findRoute.gVariables import Board,Piece
from findRoute.alphaBetaPruning import abS

if __name__ == '__main__':
    origin = (0,3)
    end = (6,3)
    """
    initialization piece and board
    """
    myPiece = Piece(0,origin)# initialization my piece 
    enemysPiece = Piece(1,end)
    myBoard = Board(origin,end) # initialization my board
    
#     myBoard.movePiece(origin, (1,5))
#     myBoard.movePiece(end, (3,1))
#     print("origin board is ")
#     print(myBoard.board)
    
    """
    place block
    """
#     myBoard.placeBlock(1, 2, 5) 
#     myBoard.placeBlock(0, 1, 4)  
#     myBoard.placeBlock(0, 3, 5)
     
    """
    possible piece location test
    """
#     res = findNeighbor(myPiece.location,myBoard)
#     print("find neighbor test result is ") #print result
#     print(res) 
    
    """
    possible blocks location test
    """
#     res = possibleBlockLocation(myPiece.location, myBoard)
#     print("possible block location test result is ")
#     print(res)
    
    """
    A* search test
    """
#     res = AStar(0,myPiece.location,myBoard)
#     print ("A* test result is ")
#     print ("res")
    
    """
    alpha beta pruning test
    """
    res = abS(2, myBoard)
    print ("alpha beta pruning test result is")
    print(res)
