'''
Created on 2019年3月17日

@author: Martha Zhao
'''
import numpy as np

"""
create board (center,right,down) 
center:0 location available 
right down ---- -1: with block 1: no block
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
    mode = 1 vertical mode = 2 horizon
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
    """
    (x0,y0) origin location
    mode:
    1: up   2: down   3: left   4: right
    """                           
    def movePiece(self,oldLocation,newLocation):
        self.board[oldLocation[0],oldLocation[1] * 3] = 0
        self.board[newLocation[0],newLocation[1] * 3] = 1
        if oldLocation == self.myPieceLocation:
            self.myPieceLocation = newLocation
            print('move my piece from'+repr(oldLocation)+' to '+repr(newLocation))
        elif oldLocation == self.enemysPieceLocation:
            self.enemysPieceLocation = newLocation
            print('move enemy"s piece from'+repr(oldLocation)+' to '+repr(newLocation))
#         else:
#             print('Wrong Move!,no piece in ',oldLocation)
#             raise Exception("movePiece Exception")
          
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
neighbor:left right up down with no blocks remove:location occupied and with blocks
f: real step up to now and vertical distance end[0] - location[0]
g: real step up to now
h: estimate distance to destination
f = g + h
destination: column to go to
function: findNeighbor find all neighbors not occupied and remove blocked
p.s. search from end to begin to avoid index jump 
"""
class Piece():
    def __init__(self,owner,location):
        self.location = location
        self.owner = owner    
        
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
