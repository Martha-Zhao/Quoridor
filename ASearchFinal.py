# -*- coding: utf-8 -*-
#A_search.py
#回溯法
from cheseBoard.gVariables import Piece,CreateBoard,origin,end

"""
A* find route
father point in list myBoard.C
son point in myPiece.neighbor
point tested in list myBoard.S
dead route in list myBoard.D
distance : shortest route among son piece  
search with backTracking
"""
# def preEdit():
#     myPiece = Piece(origin)# initialization my piece 
#     myBoard = CreateBoard(origin,end) # initialization my board
#     myBoard.placeBlock(1, 2, 3) 
#     myBoard.placeBlock(0, 3, 3)  
#     myBoard.placeBlock(1, 2, 2)
temp = 1
def searchPath(piece,board): 
    global temp
    while(temp):         
        distance = 0x3f3f3f3f
        piece.findNeighbor(board)
        if piece.neighbor != []:
            for i in piece.neighbor:
                sonPiece = Piece(i)
                board.S.append(i)
                if sonPiece.calculateDistance(board) <= distance:
                    distance = sonPiece.calculateDistance(board)
                    searchResult = i
            board.C.append(searchResult)
            if searchResult[0] == 6:
                temp= 0
            piece = Piece(searchResult)
            searchPath(piece,board)
        else:
            board.S.remove(piece.location)
            board.C.remove(piece.location)
            board.D.append(piece.location)
            piece = Piece(board.C[-1])
#             myPiece = Piece(myBoard.S[-1])
#             myBoard.C.append(myPiece.location)



#main function
# if __name__ == '__main__':

 
# result = searchPath()
# print(result) #print result  
            