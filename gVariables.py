import numpy as np

"""
create board (center,right,down) 
center:0 location available 
right down ---- -1: with block 1: no block
"""   
# myPiece = cheseBoard.test.myPiece
# myBoard = cheseBoard.test.myBoard
end = 6
class CreateBoard():
    def __init__(self,origin,end):
        a = np.array([0,1,1]) 
        b = np.array([0,-1,1])
        A = np.vstack((a,a,a,a,a,a,(0,1,-1)))
        B = np.vstack((b,b,b,b,b,b,(0,-1,-1)))
        A = np.hstack((A,A,A,A,A,A,B)) 
 
        self.board = A  
        
        self.board[origin[0],origin[1] * 3] = 1
        self.board[end[0],end[1] * 3] = 1
        self.blocksList = []
        
        self.S = [origin] # occupied
        self.C = [origin] #root decided
        self.D = [] #no root available
        
        self.row = 7
        self.column = 7
        self.origin  = origin
        self.end = end
    
    """
    mode = 1 vertical mode = 2 horizon
    (x,y) center of block
    """    
    def placeBlock(self,mode,x,y): 
        if mode == 1:     
            self.board[x,y * 3 + 1] = -1
            self.board[x + 1,y * 3 + 1] = -1
        else:
            self.board[x,y * 3 + 2] = -1
            self.board[x,y * 3 + 5] = -1
        self.blocksList.append((mode,x,y))   
    """
    (x0,y0) origin location
    mode:
    1: up   2: down   3: left   4: right
    """                           
    def movePiece(self,originalLocation,targetLocation):
        self.board[originalLocation[0],originalLocation[1] * 3] = 0
        self.board[targetLocation[0],targetLocation[1] * 3] = 1 
        
    def returnDistance(self):
        return (len(self.C))
    
"""
class Piece:
location: location of  piece
neighbor:left right up down remove:location occupied and with blocks
distance: real step up to now and vertical distance end[0] - location[0]
function: findNeighbor find all neighbors not occupied and remove blocked
p.s. search from end to begin to avoid index jump 
"""
class Piece:
    def __init__(self,location):
        self.location = location
        # neighbor
        self.neighbor = []
        self.distance = 0
        
    def calculateDistance(self,testBoard):
        x = self.location[0]
#         y = self.location[1] #test variable
        return (end - x + len(testBoard.C))
        
    def findNeighbor(self,testBoard):
        x = self.location[0]
        y = self.location[1]
        if y - 1 >= 0 and testBoard.board[x,(y - 1) * 3] == 0 and testBoard.board[x,y * 3 - 2] == 1: 
            self.neighbor.append((x,y - 1))
        if y + 1 <= testBoard.column - 1 and testBoard.board[x,(y + 1) * 3] == 0 and testBoard.board[x,y * 3 + 1] == 1:
            self.neighbor.append((x,y + 1))
        if x - 1 >= 0 and testBoard.board[x - 1,y * 3] == 0 and testBoard.board[x - 1,y * 3 + 2] == 1:
            self.neighbor.append((x - 1,y))
        if x + 1 <= testBoard.row - 1 and testBoard.board[x + 1,y * 3] == 0 and testBoard.board[x,y * 3 + 2] == 1:
            self.neighbor.append((x + 1,y))
        
        for i in reversed(self.neighbor):
            if (i in testBoard.C) or (i in testBoard.D):
                self.neighbor.remove(i)
