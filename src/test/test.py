# from cheseBoard.preBoard import *
from findRoute.ASearchFinal import *
from findRoute.gVariables import CreateBoard
origin = (0,3)
end = (6,3)
"""
initialization piece and board
"""
myPiece = Piece(origin)# initialization my piece 
myBoard = CreateBoard(origin,end) # initialization my board

myBoard.movePiece(origin, (1,5))
myBoard.movePiece(end, (3,1))
myPiece.location = (1,5)
print(myBoard.board)

"""
place block
"""
myBoard.placeBlock(1, 2, 5) 
myBoard.placeBlock(0, 1, 4)  
myBoard.placeBlock(0, 3, 5)

"""
search path test
"""
# searchPath(myPiece,myBoard)
# print(myBoard.C) #print result 

"""
possible piece location  test
"""
# result = possibleMoves(myPiece, myBoard)
# print(result)

"""
possible blocks location test
"""
result = possibleBlockLocation(myPiece, myBoard)
print(result)

