'''
Created on Mar 26, 2019
@todo: Monto-Carlo Tree Search
@author: martha
'''
from findRoute.gVariables import Board

class SearchNode():
    def __init__(self,location):
        self.winNum = 0
        self.searchNum = 0
        self.winnerRate = self.winNum/self.searchNum
        self.location = location
        self.neighbor = []
    def findNeighbor(self,tempBoard):
        self.neighbor = []
class Selection():
    def __init__(self,searchNode):
        self.searchList = searchNode.neighbor
class expantation():
    pass
class simulation():
    pass
class backpropagation():
    pass
if __name__ == '__main__':
    """
    initialization
    """
    origin = (0,3)
    end = (6,3)
    testBoard = Board(origin, end)
    rootNode = SearchNode(origin)