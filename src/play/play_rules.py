'''
Created on 2019年3月27日
# -*- coding: utf-8 -*-
@author: Martha Zhao
'''


def possibleBlockLocation(location, board, block_list):
    """
    all possible blocks location
    """
    moveList = []
    x = location[0]
    y = location[1]
    searchList = [(-3, 0), (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
                  (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1),
                  (-3, -2), (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2),
                  (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1),
                  (-3, 2), (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2)]
#     searchList = [(0, 0), (-1, 0)]
    for i in searchList:
        if (y + i[1] < 0 or y + i[1] > 5
                or x + i[0] < 0 or x + i[0] > 5
                or (0, x + i[0], y + i[1]) in block_list
                or (1, x + i[0], y + i[1]) in block_list):
            pass
        else:
            if (board[x + i[0], (y + i[1]) * 3 + 1] == 1
                    and board[x + i[0] + 1, (y+i[1])*3 + 1] == 1):
                moveList.append([1, x + i[0], y + i[1]])
            if (board[x+i[0],  (y + i[1])*3 + 2] == 1
                    and board[x+i[0], (y+i[1] + 1)*3 + 2] == 1):
                moveList.append([0, x+i[0], y+i[1]])
    return moveList


def findNeighbor(location, board):
    """
    all possible piece location
    """
    x = location[0]
    y = location[1]
    neighbor = []
    """
    down
    """
    if x < 6 and board[x, y*3 + 2] == 1:
        if board[x+1, y*3] == 0:
            neighbor.append([x+1, y])
        elif x < 5 and board[x+1, y*3] == 1:
            if board[x+1, y*3 + 2] == 1:
                neighbor.append([x+2, y])
            elif board[x+1, (y-1)*3 + 1] == 1:
                neighbor.append([x+1, y - 1])
            elif board[x+1, y*3 + 1] == 1:
                neighbor.append([x+1, y + 1])
    """
    left
    """
    if y > 0 and board[x, (y-1)*3 + 1] == 1:
        if board[x, (y-1)*3] == 0:
            neighbor.append([x, y-1])
        elif y > 1 and board[x, (y-1) * 3] == 1:
            if board[x, (y-2)*3 + 1] == 1:
                neighbor.append([x, y - 2])
            elif board[x-1, (y-1)*3 + 2] == 1:
                neighbor.append([x-1, y - 1])
            elif board[x, (y-1)*3 + 2] == 1:
                neighbor.append([x+1, y - 1])

    """
    right
    """
    if y < 6 and board[x, y*3 + 1] == 1:
        if board[x, (y+1)*3] == 0:
            neighbor.append([x, y + 1])
        elif y < 5 and board[x, (y+1)*3] == 1:
            if board[x, (y+1)*3 + 1] == 1:
                neighbor.append([x, y + 2])
            elif board[x-1, (y+1)*3 + 2] == 1:
                neighbor.append([x-1, y + 1])
            elif board[x, (y+1)*3 + 2] == 1:
                neighbor.append([x+1, y + 1])

    """
    up
    """
    if x > 0 and board[x-1, y*3 + 2] == 1:
        if board[x-1, y*3] == 0:
            neighbor.append([x - 1, y])
        elif x > 1 and board[x - 1, y*3] == 1:
            if board[x - 2, y*3 + 2] == 1:
                neighbor.append([x - 2, y])
            elif board[x - 1, (y-1)*3 + 1] == 1:
                neighbor.append([x - 1, y - 1])
            elif board[x - 1, y*3 + 1] == 1:
                neighbor.append([x - 1, y + 1])

    return neighbor


"""
test IN
"""
# from play.board import Board
# if __name__ == '__main__':
#     test_board = Board()
#     test_board.move_piece(0, [6, 3])
#     test_board.move_piece(1, [0, 3])
#     test_board.place_blocks(1, [1, 1, 3])
#     print(test_board.board)
#     print(test_board._player)
#     print(test_board.block_list)
#     print(test_board.is_game_over())
#     print(findNeighbor((0, 3), test_board.board))
#     print(possibleBlockLocation((0, 3),
#                                 test_board.board, test_board.block_list))
