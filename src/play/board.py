'''
Created on Mar 27, 2019
@title: class board Initialization
@author: martha
'''
import numpy as np
AI_START = [0, 3, 10, 6]
PLAYER_START = [6, 3, 10, 0]


class Board():
    """define general rules of game
    """
    a = np.array([0, 1, 1])
    b = np.array([0, -1, 1])
    A = np.vstack((a, a, a, a, a, a, (0, 1, -1)))
    B = np.vstack((b, b, b, b, b, b, (0, -1, -1)))
    origin_board = np.hstack((A, A, A, A, A, A, B))

    def __init__(self):
        self.board = self.origin_board  # 构建 棋盘
        self._player = {0: AI_START,  # AI location
                        1: PLAYER_START}  # player's location
#         self.board[0][3 * 3] = 1  # place AI's piece
#         self.board[6][3 * 3] = 1  # place enemy's piece

        self.block_list = []  # blocks already placed

    def is_game_over(self):  # if game is over return 1; else return 0
        for key, items in self._player.items():
            if items[0] == items[3]:
                print(key, "  win!")
                return 1
        return 0

    def restart(self):  # restart game
        self.current_player = 1  # 玩家先手
        self.last_player = 0  # AI后手
        self.board = self.origin_board
        self.board[0][3 * 3] = 1
        self.board[6][3 * 3] = 1
        self._player = {0: AI_START,
                        1: PLAYER_START}
        self.block_list = []

    def place_blocks(self, turn, action):  # place an block action = [mode, x, y]
        mode = action[0]
        x = action[1]
        y = action[2]
        if self._player[turn][2] < 1:  # turn has no block left
            print(turn, ' has no blocks left')
        else:
            if mode == 1:  # place a vertical block
                self.board[x, y*3 + 1] = -1
                self.board[x + 1, y*3 + 1] = -1
            else:  # place horizon block
                self.board[x, y*3 + 2] = -1
                self.board[x, y*3 + 5] = -1
            self.block_list.append((mode, x, y))  # add new block in block list
            self._player[turn][2] -= 1  # turn's block number minus one

    def remove_blocks(self, turn, action):   # remove blocks refresh board
        mode = action[0]
        x = action[1]
        y = action[2]
        if mode == 1:
            self.board[x, y*3 + 1] = 1
            self.board[x + 1, y*3 + 1] = 1
        else:
            self.board[x, y*3 + 2] = 1
            self.board[x, y*3 + 5] = 1
        self.block_list.remove((mode, x, y))
        self._player[turn][2] += 1

    def delete_piece(self, action):  # delete piece in x, y
        self.board[action[0]][action[1] * 3] = 0

    def add_piece(self, action):  # add piece in x, y
        self.board[action[0]][action[1] * 3] = 1

    def move_piece(self, turn, action):  # move turn's piece to x, y
        x = action[0]
        y = action[1]
        self.board[self._player[turn][0]][self._player[turn][1] * 3] = 0
        self.board[x][y * 3] = 1
        self._player[turn][:2] = [x, y]

    def delete_all_piece(self):
        for _, value in self._player.items():
            self.board[value[0]][value[1]*3] = 0

    def restore_all_piece(self):
        for _, value in self._player.items():
            self.board[value[0]][value[1]*3] = 1

    def get_move(self, turn, action):
        if len(action) == 2:
            self.move_piece(turn, action)
        else:
            self.place_blocks(turn, action)


if __name__ == '__main__':
    testBoard = Board()
    testBoard.replace_store_piece()
    print(testBoard.board)
