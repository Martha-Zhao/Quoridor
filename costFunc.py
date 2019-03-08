'''
#Created on 

@author: Martha Zhao
'''

import numpy as np

def createBoard():
    a = np.array([1,0,0])
    b = np.array([0,1,-1])
    A = np.vstack((a,a,a,a,a,a,(1,-1,0)))
    B = np.vstack((b,b,b,b,b,b,(1,-1,-1)))
    A = np.hstack((A,A,A,A,A,A,B))
    return A

print(createBoard())
