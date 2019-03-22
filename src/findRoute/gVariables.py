'''
Created on 2019年3月17日

@author: Martha Zhao
'''
import numpy as np

"""
class Board initialization board 
initialization with my piece's location and enemy's piece's location
if  board(x,y * 3) == 1: have piece in (x,y)
    board(x,y * 3) == 0: no piece in (x,y)
openList: A* searched location (possible moves)
closeList: A* defined location (identified moves)
blocksList: already placed blocks location
            (mode,x,y) mode: 0--horizon 1--vertical
                      (x,y): center of block 
myPieceLocation: location of my piece
enemysPieceLocation: location of enemy's piece
myBlockNum: number of my blocks in hands (10-used)
enemysBlockNum: number of enemy's blocks in hands (10 - used)
            length(blocksList) = myUsed + enemy'sUsed


"""   
class Board():
    def __init__(self,myPieceLocation,enemysPieceLocation):
        a = np.array([0,1,1]) 
        b = np.array([0,-1,1])
        A = np.vstack((a,a,a,a,a,a,(0,1,-1)))
        B = np.vstack((b,b,b,b,b,b,(0,-1,-1)))
        A = np.hstack((A,A,A,A,A,A,B)) 
        self.board = A 
        self.board[myPieceLocation[0],myPieceLocation[1] * 3] = 1
        self.board[enemysPieceLocation[0],enemysPieceLocation[1] * 3] = 1
        self.openList = []
        self.closeList = []
        self.blocksList = []   
        self.myPieceLocation = myPieceLocation
        self.enemysPieceLocation = enemysPieceLocation 
        self.myBlockNum = 10
        self.enemysBlockNum = 10
             
    """
    place an block in (mode,x,y)
    owner's block number -1
    blocks list append (mode,x,y)
    owner: 0: my block;    1: enemy's block
    mode : 1: vertical;    2: horizon
    (x,y) center of block
    """    
    def placeBlock(self,owner,mode,x,y): 
        if (not owner) and self.myBlockNum <= 0: #owner = 0 my turn 
            print('My blocks has run out! ')
            raise Exception("place Blocks Exception")
        elif owner and self.enemysBlockNum <=0:
            print('Enemy"s blocks has run out! ')
            raise Exception("place Blocks Exception")
        else:
            if mode == 1:     
                self.board[x,y * 3 + 1] = -1
                self.board[x + 1,y * 3 + 1] = -1
            else:
                self.board[x,y * 3 + 2] = -1
                self.board[x,y * 3 + 5] = -1
            self.blocksList.append((mode,x,y))
            if not owner:
                self.myBlockNum -= 1
            else:
                self.enemysBlockNum -= 1
#             print(repr(owner) + " place an block in " + repr((mode,x,y)))
    """
    remove block (owner,mode,x,y)
    remove block (mode,x,y)
    owner's block number + 1
    blocksList remove (mode,x,y)
    """        
    def removeBlock(self,owner,mode,x,y):
        if mode == 1:     
            self.board[x,y * 3 + 1] = 1
            self.board[x + 1,y * 3 + 1] = 1
        else:
            self.board[x,y * 3 + 2] = 1
            self.board[x,y * 3 + 5] = 1
        if not owner:
            self.myBlockNum += 1
        else:
            self.enemysBlockNum += 1
        self.blocksList.remove((mode,x,y))
#         print(repr(owner) + ' remove an block on '+ repr((mode,x,y)))

       
    """
    move piece (owner,oldLocation,newLocation)
    set piece in new location
    remove owner's piece in old location
    renew owner's piece's location with new location
    """                           
    def movePiece(self,owner,oldLocation,newLocation):
        self.board[oldLocation[0],oldLocation[1] * 3] = 0
        self.board[newLocation[0],newLocation[1] * 3] = 1
        if not owner:
            self.myPieceLocation = newLocation
        else:
            self.enemysPieceLocation = newLocation

    """
    delete piece in old location
    uses in restore board
    """
    def delPiece(self,oldLocation):
        self.board[oldLocation[0],oldLocation[1] * 3] = 0
#         print ('remove piece located in ',oldLocation)

    """
    set piece in new location
    used in restore board
    """
    def setPiece (self,newLocation):
        self.board[newLocation[0],newLocation[1] * 3] = 1
#         print ('set piece located in ',newLocation)   
        
    """
    define whether game is over
    if my piece location column 6 return 1
    if enemy's piece location column 0 return 0
    else:
    return 0
    """   
    def isGameOver(self):
        if self.myPieceLocation[0] == 6:
            print("AI win!") 
            return 1
        elif self.enemysPieceLocation[0] == 0:
            print("Player win!")
            return 1
        else:
            return 0
            
            
"""
class Point:
location: location of  piece
owner: 0---my piece   1---enemy's piece
"""
class Piece():
    def __init__(self,owner,location):
        self.location = location
        self.owner = owner
            
"""
class point
neighbor:left right up down with no blocks remove:location occupied and with blocks
f: real step up to now and vertical distance end[0] - location[0]
g: real step up to now
h: estimate distance to destination
f = g + h
destination: column to go to
"""        
class Point():
    def __init__(self,owner,location):
        self.location = location
        self.fatherPoint = None
        if owner:#enemy's piece
            self.destination = 0
            self.h = location[0]
        else: # my piece
            self.destination = 6
            self.h = self.destination - location[0]
        self.g = 0
        self.f = 0
