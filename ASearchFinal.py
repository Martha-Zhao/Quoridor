# -*- coding: utf-8 -*-
#A_search.py
#回溯法
from findRoute.gVariables import Piece
"""
A* find route
father point in list myBoard.C
son point in myPiece.neighbor
point tested in list myBoard.S
dead route in list myBoard.D
distance : shortest route among son piece  
search with backTracking
"""

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

def possibleMoves(piece,testBoard):
    moveList = []
    x = piece.location[0]
    y = piece.location[1]
    """
    up
    """
    if testBoard.board[x - 1,y * 3] == 1 and x > 0:  #piece upon
        if testBoard.board[x - 2,y * 3 + 2] == -1 and x > 1: # block upon upon 
            if testBoard.board[x - 1,y * 3 - 2] == 1 and y > 0:  #up left
                moveList.append((x - 1,y - 1))
            if testBoard.board[x - 1,y * 3 + 1] == 1: #up right
                moveList.append((x - 1,y + 1))
        elif x > 1:
            moveList.append((x - 2,y)) #up up
    elif testBoard.board[x - 1,y * 3 + 2] == 1 and x > 0: 
        moveList.append((x - 1,y))# up
        
    """
    down
    """
    if testBoard.board[x + 1, y * 3] == 1 and x < 6: #piece blow
        if testBoard.board[x + 1, y * 3 + 2] == -1 : # block blow blow
            if testBoard.board[x + 1,y * 3 - 2] == 1 and y > 0: #up left
                moveList.append((x + 1,y - 1))
            if testBoard.board[x + 1,y * 3 + 1] == 1:
                moveList.append((x + 1,y + 1))  #up right
        elif x < 5:
            moveList.append((x + 2,y))        
    elif testBoard.board[x, y * 3 + 2] == 1 and x < 6:
        moveList.append((x + 1 ,y))
    """
    left
    """
    if testBoard.board[x,(y - 1) * 3] == 1 and y > 0: #piece left
        if testBoard.board[x,(y - 2) * 3 + 1] == -1 and y > 1: #block left left
            if testBoard.board[x - 1,(y - 1) * 3 + 2] == 1 and x > 0: # left upon
                moveList.append((x - 1,y - 1))
            if testBoard.board[x,(y - 1) * 3 + 2] == 1: # left blow
                moveList.append((x + 1,y - 1))
        elif y > 1:
            moveList.append((x, y - 2)) #left left
    elif testBoard.board[x, (y - 1)* 3 + 1] == 1 and y > 0:
        moveList.append((x,y - 1)) #left
        
    """
    right
    """
    if testBoard.board[x,(y + 1) * 3] == 1 and y < 6:  #piece right
        if testBoard.board[x,(y + 1) * 3 + 1] == -1: #block right right
            if testBoard.board[x - 1,(y + 1) * 3 + 2] == 1 and x > 0: #right upon
                moveList.append((x - 1,y + 1))
            if testBoard.board[x,(y + 1) * 3 + 2] == 1: # right blow
                moveList.append((x + 1,y + 1))
        elif y < 5:
            moveList.append((x,y + 2)) #right right 
    elif testBoard.board[x,y * 3 + 1] == 1 and y < 6:
        moveList.append((x, y + 1)) # right
    return moveList

def possibleBlockLocation(piece,testBoard):
    moveList = []
    x = piece.location[0]
    y = piece.location[1]
    searchList = [(-2,0),(-1,0),(0,0),(1,0),
                  (-2,-1),(-1,-1),(0,-1),(1,-1),
                  (-2,-2),(-1,-2),(0,-2),(1,-2),
                  (-2,1),(-1,1),(0,1),(1,1),
                  (-2,2),(-1,2),(0,2),(1,2)]
    for i in searchList:
        if y + i[1] < 0 or y + i[1] > 5 or x + i[0] < 0 or x + i[0] > 5 or (0,x + i[0],y + i[1]) in testBoard.blocksList or (1,x + i[0],y + i[1]) in testBoard.blocksList:
            pass
        else:
            if testBoard.board[x + i[0] ,(y + i[1]) * 3 + 1] == 1 and testBoard.board[x + i[0] + 1 ,(y + i[1]) * 3 + 1] == 1:
                moveList.append((1,x + i[0],y + i[1]))
            if testBoard.board[x + i[0] ,(y + i[1]) * 3 + 2] == 1 and testBoard.board[x + i[0],(y + i[1] + 1) * 3 + 2] == 1:
                moveList.append((0,x + i[0],y + i[1]))
    return moveList    
    
