'''
Created on 2019年3月22日

@author: Martha Zhao
@todo: all the test available
'''

# from cheseBoard.preBoard import 
from findRoute.AStar import findNeighbor,possibleBlockLocation,AStar
from findRoute.gVariables import Board,Piece
from findRoute.alphaBetaPruning import abS
from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    origin = (0,3)
    end = (6,3)
    """
    initialization piece and board
    """
    myPiece = Piece(0,(0,3))# initialization my piece 
    enemysPiece = Piece(1,(6,3))
    myBoard = Board(origin,end) # initialization my board
    
#     myBoard.movePiece(0, (1,3))
#     myBoard.movePiece(1, (5,3))
#     print("origin board is ")
#     print(myBoard.board)
    
    """
    place block
    """
#     myBoard.placeBlock(0, 1, 5, 4) 
    myBoard.placeBlock(1, 0, 1, 3)  
    myBoard.placeBlock(1, 1, 1, 4) 
#     myBoard.placeBlock(0, 3, 5)
     
    """
    possible piece location test
    """
#     print(myBoard.board)
#     res = findNeighbor(0,myBoard.myPieceLocation,myBoard)
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
#     res = AStar(0,myBoard.myPieceLocation,myBoard)
#     print ("A* test result is ")
#     print (res)
    
    """
    alpha beta pruning test
    """
#     res = abS(2, myBoard)
#     print ("alpha beta pruning test result is")
#     print(res)
    """
    system in test
    """
#     sysInPut = raw_input("enemy's action is :")
#     sysInPut = str.split(',')
#     enemyMove = [int(sysInPut[i]) for i in range(len(sysInPut)) ]
#     print (enemyMove)
           
#     print()
    """
    play test
    """
    while(not myBoard.isGameOver()):
#        my step
        res = abS(2, myBoard)
        print ("alpha beta pruning test result is",res)
        if len(res) == 2:
            myBoard.movePiece(0, res)
        else:
            myBoard.placeBlock(0, res[0], res[1], res[2])
#        enemy's step
        enemyStepInString = raw_input("Please input enemy's step : ")
        enemyStepInList = enemyStepInString.split(',')
        enemyStepList = [int(enemyStepInList[i]) for i in range(len(enemyStepInList))]
        print ("Enemy's step is :",enemyStepList)
        if len(enemyStepList) == 2:
            myBoard.movePiece(1, enemyStepList)
        else:
            myBoard.placeBlock(1, enemyStepList[0], enemyStepList[1], enemyStepList[2])
             
          
        
