# -*- coding: utf-8 -*-
#A_search.py

import numpy as np

A = np.array([[0,0,0,0,1,0,0],  #map
              [0,0,0,1,0,0,0],
              [0,1,0,1,0,1,1],
              [0,0,0,1,0,0,0],
              [0,1,0,0,0,1,0]])


origin = (0,0)
end  = (4,6)        
S = [origin]
C = [origin]
D = []

searchCount = 0

class Piece:
    def __init__(self,location):
        self.location = location
        # neighbor
        self.neighbor = []
        self.distance = 0
        a = self.location[0]   #location x
        b = self.location[1]   #location y
        if a - 1 >= 0 and A[a - 1,b] == 0: #search neighbors available
            self.neighbor.append((a - 1,b))
        if a + 1 <= 4 and A[a + 1,b] == 0:
            self.neighbor.append((a + 1,b))
        if b - 1 >= 0 and A[a,b - 1] == 0:
            self.neighbor.append((a,b - 1))
        if b + 1 <= 6 and A[a,b + 1] == 0:
            self.neighbor.append((a,b + 1))
        for i in self.neighbor:
            if (i in S) or (i in C) or (i in D):
                self.neighbor.remove(i)
            

 
#回溯法
# fatherPiece = origin
myPiece = Piece((origin))  
def searchPath():
#     print(myPiece)
    global searchCount
    global myPiece
    if end in S:
        return 0   #print
    else:
#         searchCount = searchCount + 1
        searchCount = 0
        distance = 0x3f3f3f
        if myPiece.neighbor != []:
            for i in myPiece.neighbor:
                sonPiece = Piece(i)
                S.append(i)
                sonPiece.distance =  searchCount + end[0] - sonPiece.location[0] + end[1] - sonPiece.location[1]
                if sonPiece.distance <= distance:
                    distance = sonPiece.distance
                    searchResult = i
            C.append(searchResult)
            myPiece = Piece(searchResult)
            searchPath()
        else:
            pass
            S.remove(myPiece.location)
            C.remove(myPiece.location)
            D.append(myPiece.location)
            myPiece = Piece(S[len(S) - 1])



if __name__ == "__main__":
#     myPiece = Piece((origin))  
    searchPath()       
