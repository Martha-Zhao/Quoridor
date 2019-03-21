'''
Created on 2019年3月17日

@author: Martha Zhao
'''

from findRoute.gVariables import Point

def possibleBlockLocation(location,testBoard):
    moveList = []
    x = location[0]
    y = location[1]
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
  
def findNeighbor(location,testBoard):
    x = location[0]
    y = location[1]
    neighbor = []   
    """
    down
    """
    if x < 6 and testBoard.board[x,y * 3 + 2] == 1:
        if  testBoard.board[x + 1,y * 3] == 0:
            neighbor.append((x + 1,y))
        elif x < 5 and testBoard.board[x + 1,y * 3] == 1:
            if testBoard.board[x + 1,y * 3 + 2] == 1:
                neighbor.append((x + 2,y))
            elif testBoard.board[x + 1,(y - 1) * 3 + 1] == 1:
                neighbor.append((x + 1,y - 1))
            elif testBoard.board[x + 1,y * 3 + 1] == 1:
                neighbor.append((x + 1,y + 1))
    """
    left
    """
    if y > 0 and testBoard.board[x,(y - 1) * 3 + 1] == 1:
        if  testBoard.board[x,(y - 1) * 3] == 0:
            neighbor.append((x,y - 1))
        elif y > 1 and testBoard.board[x,(y - 1) * 3] == 1:
            if testBoard.board[x,(y - 2) * 3 + 1] == 1:
                neighbor.append((x,y - 2))
            elif testBoard.board[x - 1,(y - 1) * 3 + 2] == 1:
                neighbor.append((x - 1,y - 1))
            elif testBoard.board[x,(y - 1) * 3 + 2] == 1:
                neighbor.append((x + 1,y - 1))
        
    """
    right
    """
    if y < 6 and testBoard.board[x,y * 3 + 1] == 1:
        if  testBoard.board[x,(y + 1) * 3] == 0:
            neighbor.append((x,y + 1))
        elif y < 5 and testBoard.board[x,(y + 1) * 3] == 1:
            if testBoard.board[x,(y + 1) * 3 + 1] == 1:
                neighbor.append((x,y + 2))
            elif testBoard.board[x - 1,(y + 1) * 3 + 2] == 1:
                neighbor.append((x - 1,y + 1))
            elif testBoard.board[x,(y + 1) * 3 + 2] == 1:
                neighbor.append((x + 1,y + 1))
        
    """
    up
    """
    if x > 0 and testBoard.board[x - 1,y * 3 + 2] == 1:
        if  testBoard.board[x - 1,y * 3] == 0:
            neighbor.append((x - 1,y))
        elif x > 1 and testBoard.board[x - 1,y * 3] == 1:
            if testBoard.board[x -2,y * 3 + 2] == 1:
                neighbor.append((x - 2,y))
            elif testBoard.board[x - 1,(y - 1) * 3 + 1] == 1:
                neighbor.append((x - 1,y - 1))
            elif testBoard.board[x - 1,y * 3 + 1] == 1:
                neighbor.append((x - 1,y + 1))
                
    return neighbor
          
def AStar(owner,origin,testBoard):
    temp = 1
#     searchPiece = Piece(owner,origin) #initialization start piece
#     fatherPiece = searchPiece
#     testBoard.closeList.append(fatherPiece) #add start point to open list
    searchPoint = Point(owner,origin)
#     searchPoint.fatherPoint = searchPoint
    testBoard.closeList.append(searchPoint)
    while temp:
        sonPointInOpenlistFlag = 0
        neighbor = findNeighbor(searchPoint.location,testBoard)
        for i in neighbor:
            sonPointInOpenlistFlag = 0
            sonPoint = Point(owner,i)
            sonPoint.fatherPoint = searchPoint.location
            sonPoint.g = searchPoint.g + 1
            sonPoint.f = sonPoint.g + sonPoint.h
            
            if sonPoint.location[0] == searchPoint.destination:
                temp = 0
#                 break
            for searchRepeat in testBoard.openList:
                if sonPoint.location == searchRepeat.location:
                    sonPointInOpenlistFlag = 1
                    if sonPoint.g < searchRepeat.g:
                        searchRepeat.fatherPoint = searchPoint.location
                        searchRepeat.g = searchPoint.g + 1
                        searchRepeat.f = searchRepeat.g + searchRepeat.h
                    break
            if not sonPointInOpenlistFlag:
                testBoard.openList.append(sonPoint)
                
 
        minimalSearch = 0x3f3f3f3f
        for tempPoint in testBoard.openList:
            if tempPoint.f <= minimalSearch:
                searchPoint = tempPoint
                minimalSearch = tempPoint.f
        testBoard.openList.remove(searchPoint)
        testBoard.closeList.append(searchPoint) 
        tempPoint = testBoard.closeList[-1]  
        result = [tempPoint.location] 
#         testBoard.movePiece(searchPoint.location,result)
    while not (tempPoint.location == origin):
        result.append(tempPoint.fatherPoint)
        for i in reversed(testBoard.closeList):
            if i.location == tempPoint.fatherPoint:
                tempPoint = i
                testBoard.closeList.remove(i)
                break
    print(result)
    testBoard.openList = []
    testBoard.closeList = []
    return len(result) - 1 #return distance
#         tempPoint = testBoard.closeList[testBoard.closeList.index(tempPoint.fatherPoint)]

def evaluationFunc(testBoard):
    testBoard.delPiece(testBoard.myPieceLocation)
    myStep = AStar(0, testBoard.myPieceLocation, testBoard)
#     print('my step is ',myStep)
    testBoard.setPiece(testBoard.myPieceLocation)
    testBoard.delPiece(testBoard.enemysPieceLocation)
    enemyStep = AStar(1, testBoard.enemysPieceLocation, testBoard)
#     print('enemy"s step is ',enemyStep)
    testBoard.setPiece(testBoard.enemysPieceLocation)
    return enemyStep - myStep
