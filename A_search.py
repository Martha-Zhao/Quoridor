# -*- coding: utf-8 -*-
#A_search.py

import numpy as np

A = np.array([[0,0,0,0,1,0,0],  #map
              [0,0,0,1,0,0,0],
              [0,1,0,1,0,1,1],
              [0,0,0,1,0,0,0],
              [0,1,0,0,0,1,0]])

S = []   #to be searched
C = [(0,0)] # Choose
origin = (0,0) #start point
end = (4,6) #end point

g = np.array([[0,0,0,0,0,0,0],  #g(x) Distance from origin to x
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0]]) 

f = np.array([[0,0,0,0,0,0,0],  #f(x) Distance from begin to end across x
              [0,0,0,0,0,0,0],  #f(x) = g(x) + h(x)
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0]])
                                                          
class Piece():    #class x
    def __init__(self,father,itself):
        self.father = father   #father point
        self.itself = itself #ltself's location
        self.son = origin
        #calculate neighbors available
        self.neighbor = []   #array of neighbor 
        a = self.itself[0]   #location x
        b = self.itself[1]   #location y
        if a - 1 >= 0 and A[a - 1,b] == 0: #search neighbors available
            self.neighbor.append((a - 1,b))
        if a + 1 <= 4 and A[a + 1,b] == 0:
            self.neighbor.append((a + 1,b))
        if b - 1 >= 0 and A[a,b - 1] == 0:
            self.neighbor.append((a,b - 1))
        if b + 1 <= 6 and A[a,b + 1] == 0:
            self.neighbor.append((a,b + 1))
        for i in self.neighbor:
            if (i in S) or(i in C):
                self.neighbor.remove(i)
        S = S + self.neighbor
    def calculateDistance(self):  #calculate f(x)
        g[self.itself[0],self.itself[1]] = g[self.father[0],self.father[1]] + 1
        f[self.itself[0],self.itself[0]] = 10 - self.itself[0] - self.itself[1] + g[self.itself[0],self.itself[1]]
#         return f[self.itself[0],self.itself[0]]

    #print function
    def printFather(self):
        print(self.father)    
    def printItself(self):
        print(self.itself)  
    def printNeighbor(self):  
        print(self.neighbor)
    def printDistance(self):
        self.calculateDistance()
        print(f[self.itself[0],self.itself[0]])
    def printAll(self):
        print("Father: ",self.father)
        print("Itself: ",self.itself)
        print("Neighbor: ",self.neighbor)
        print("Distance: ",end = ' ')
        self.printDistance()
        
Distance = 0x3f3f3f3f 

myPieceNow  = Piece(origin,origin)

for i in S:
    pass

# while end not in S:
# #     myPieceNow.calculateDistance()
# #     myPieceNow.myBestSon()
#     myPieceNow = Piece(myPieceNow.itself,myPieceNow.son)
# print(g)

