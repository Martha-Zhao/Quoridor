'''
Created on 2019年3月17日
@tudo: A Star 路径规划，用做simulation对于棋盘局面的评估
@author: Martha Zhao
'''
from play.play_rules import findNeighbor
from play.board import Board


class Point():
    """
    class point
    neighbor:left right up down with no blocks
    remove:location occupied and with block
    f: real step up to now and vertical distance end[0] - location[0]
    g: real step up to now
    h: estimate distance to destination
    f = g + h
    destination: column to go to
    """
    def __init__(self, owner, location):
        self.owner = owner
        self.location = location
        self.fatherPoint = None
        if owner:  # enemy's piece
            self.destination = 0
            self.h = location[0]
        else:  # my piece
            self.destination = 6
            self.h = self.destination - location[0]
        self.g = 0
        self.f = 0


class static():
    """
    board static
    """
    def __init__(self, board):
        self.board = board
        self.open_list = []
        self.close_list = []


def AStar(owner, origin, test_static):
    """
    AStar search
    return steps from now location to destination
    """
    temp = 1
    calculate_count = 0
    searchPoint = Point(owner, origin)
    test_static.close_list.append(searchPoint)
    while temp:
        sonPointInOpenlistFlag = 0
        if calculate_count > 128:
            print("Stuck in loop! Illegal move")
            return 1000
        calculate_count += 1
        neighbor = findNeighbor(searchPoint.location, test_static.board)
        if neighbor == []:
            print("No road available! Illegal move")
            return 1000
        for i in neighbor:
            sonPointInOpenlistFlag = 0
            sonPoint = Point(owner, i)
            sonPoint.fatherPoint = searchPoint.location
            sonPoint.g = searchPoint.g + 1
            sonPoint.f = sonPoint.g + sonPoint.h

            if sonPoint.location[0] == searchPoint.destination:
                temp = 0
                test_static.open_list.append(sonPoint)
                break
            for searchRepeat in test_static.open_list:
                if sonPoint.location == searchRepeat.location:
                    sonPointInOpenlistFlag = 1
                    if sonPoint.g < searchRepeat.g:
                        searchRepeat.fatherPoint = searchPoint.location
                        searchRepeat.g = searchPoint.g + 1
                        searchRepeat.f = searchRepeat.g + searchRepeat.h
                    break
            if not sonPointInOpenlistFlag:
                test_static.open_list.append(sonPoint)

        minimalSearch = 0x3f3f3f3f
        for tempPoint in test_static.open_list:
            if tempPoint.f <= minimalSearch:
                searchPoint = tempPoint
                minimalSearch = tempPoint.f
        test_static.open_list.remove(searchPoint)
        test_static.close_list.append(searchPoint)
        tempPoint = test_static.close_list[-1]
        result = [tempPoint.location]

    while not (tempPoint.location == origin):
        result.append(tempPoint.fatherPoint)
        for i in reversed(test_static.close_list):
            if i.location == tempPoint.fatherPoint:
                tempPoint = i
                del test_static.close_list[test_static.close_list.index(i):]
                break

    test_static.open_list = []
    test_static.close_list = []
#     print(result)
    return len(result) - 1  # return distance


"""
function IN
title eveluation_func
return enemy's step - my step
"""


def eveluation_func(testBoard):

#     [mylocation_x, mylocation_y] = testBoard._player[0][:2]
#     [enemylocation_x, enemylocation_y] = testBoard._player[1][:2]
    testBoard.delete_all_piece()
    test_static = static(testBoard.board)
    myStep = AStar(0, testBoard._player[0][:2], test_static)
#     print('my step is ',myStep)
    enemyStep = AStar(1, testBoard._player[1][:2], test_static)
    testBoard.restore_all_piece()
#     print('enemy"s step is ',enemyStep)
    if enemyStep == 1000 or myStep == 1000:
        return 1000
    elif enemyStep > myStep:
        return 1
    elif enemyStep == myStep:
        return 0
    else:
        return -1


# """
# test in
# """
# if __name__ == '__main__':
#     testBoard = Board()
#     testBoard.move_piece(0, [3, 2])
#     testBoard.place_blocks(1, [0, 2, 1])
#     testBoard.place_blocks(1, [1, 2, 2])
#     testBoard.place_blocks(1, [1, 3, 1])
#     testBoard.place_blocks(1, [0, 3, 2])
#     print(eveluation_func(testBoard))
