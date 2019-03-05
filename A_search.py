# -*- coding: utf-8 -*-
#helloworld.py

import numpy as np

A = np.array([[0,0,0,0,1,0,0],
             [0,0,0,1,0,0,0],
             [0,1,0,1,0,1,1],
             [0,0,0,1,0,0,0],
             [0,1,0,0,0,1,0]])

(x,y) = (0,0)

S = [(0,0)]
C = [(0,0)]

def S_add((x,y)):
    if ((x + 1,y) not in S) and ((x + 1,y) not in C and (A[x + 1,y] == 0)):
        S.append((x + 1 , y))
    if ((x,y + 1) not in S) and ((x,y + 1) not in C and (A[x,y + 1] == 0)):
        S.append((x,y + 1))
        
def C_add((x,y)):
    S.remove((x,y))
    C.append((x,y))
        
#def search((x,y)):
#    if (4,6) in S:
#        return 0
#    else:
#        
#        S_add((x,y))
        
S.append((1,1))
print("S = ",S)
C_add((1,1))
print("S = ",S)
print("C = ",C) 
