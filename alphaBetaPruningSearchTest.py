'''
Created on 2019年3月19日

@author: Martha Zhao
'''

board  =[[[[3,17],[2,0]],[[15],[20,1]]],
         [[[2,5],[3]],[[2,8]]]]
depth = 4
tempBoard = board
alpha = -0x3f3f3f
beta = 0x3f3f3f

def search(depth):
    if depth%2:
        res = minSearch(depth,tempBoard,alpha,beta)
    else:
        res = maxSearch(depth,tempBoard,alpha,beta)
    return(res)
        
def minSearch(depth,board,alpha,beta):
    choice = None
    result = None
    if depth <= 0:
        return board
    else:
        moveList = makeNextMove(board)
        for i in moveList:
            val = maxSearch(depth - 1, board[i],alpha,beta)
            if val < beta:
                beta = val
                result = board[i]
                choice = i
                if alpha >= beta :
                    break
        if depth == 4 and i ==1:
            print("choice is "+repr(choice)+ "result = "+repr(result))
        return beta
def maxSearch(depth,board,alpha,beta):
    choice = None
    result = None
    if depth <= 0:
        return board
    else:
        moveList = makeNextMove(board)
        for i in moveList:
            val = minSearch(depth - 1, board[i],alpha,beta)
            if val > alpha:
                alpha = val
                result = board[i]
                choice = i
                if alpha >= beta:
                    break
        if depth == 4 and i == 1:
            print("choice is "+repr(choice)+"result = "+repr(result))
        return alpha

def makeNextMove(tempBoard):
    moveList = []
    for i in range(len(tempBoard)):
        moveList.append(i)
    return moveList

if __name__ == '__main__':
    print(search(4))
