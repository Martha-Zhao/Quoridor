'''
Created on Mar 28, 2019
@title: pure MCTS
@tudo: Monte-Carlo Tree Search without machine learning
@author: martha
'''
from math import sqrt, log
# import numpy as np
# from random import choice
from play.play_rules import findNeighbor, possibleBlockLocation
from play.board import Board
from mcts_my.AStar import eveluation_func


class TreeNode():
    """
    BASIC class TreeNode
    initialization :
        instance: turn whose turn for this step
                  parent: parent node for this node
                  action: this node's action
                  state: temp state related on this node
    """
    def __init__(self, turn, parent, action, state):
        self._turn = turn
        self._action = action
        self._parent_node = parent
        self._child_action = []  # a map from action to TreeNode
        self._child_node = []
        self._wins = 0
        self._visits = 0
        self._state = state
        self._reset_piece_location = []

    def possible_moves(self):
        """
        method: possible moves
        possible moves for this player
        continue with piece list with length of 2
        and block list with length of 3
        """
        location = self._state._player[self._turn][:2]
        enemy_location = self._state._player[1-self._turn][:2]
        state = self._state
        piece_list = findNeighbor(location, state.board)
        block_list = possibleBlockLocation(enemy_location,
                                           state.board,
                                           state.block_list)
        self.move_list = piece_list + block_list
#         self.move_list = block_list

    def UCT_select_child(self):
        """ Use the UCB1 formula to select a child node.
            Often a constant UCTK is applied so we have
            lambda c: c.wins/c.visits + UCTK * sqrt(2*log(self.visits)/c.visits
            to vary the amount of
            exploration versus exploitation.
        """
        max_value = -0x3f3f3f
        for temp_node in self._child_node:
            value = temp_node._wins/temp_node._visits \
                + sqrt(1*log(self._visits)/temp_node._visits)
            if value > max_value:
                max_value = value
                action = temp_node._action
                select_node = temp_node
        self._state.get_move(self._turn, action)
        select_node._turn = 1-self._turn
        select_node._parent_node = self
        select_node._action = action
        return select_node

    def expend_child(self):
        """
        if this node is leaf node than it should be expended:
        expend with possible_action within possible_moves list and not searched yet
        """
        for possible_action in reversed(self.move_list):
            if possible_action not in self._child_action:
                expend_state = self._state
                if len(possible_action) == 3 and self._state._player[self._turn][2] == 0:
                    self.move_list.remove(possible_action)
                    continue
                expend_state.get_move(self._turn, possible_action)
                expend_node = TreeNode(1-self._turn,
                                       self, possible_action,
                                       expend_state)
                self._child_action.append(possible_action)
                self._child_node.append(expend_node)
                return expend_node
#                 break

    def simulation_(self):
        """
        simulation:
        board judge with enemy's step minus my step
        if it's enemy's turn than return -point
        """
        point = eveluation_func(self._state)
#         return point
        if self._turn:
            return point
        else:
            return -point

    def update(self, value):
        """
        update value to all parent's value 
        """
        if self._parent_node is not None:
            self._parent_node.update(value)
        self._visits += 1
        self._wins += value

    def reset_board(self, turn, reset_location, action):
        """
        after simulation reset board as board before simulation
        """
        if len(action) == 2:
            self._state.move_piece(turn, reset_location)
        else:
            self._state.remove_blocks(turn, action)

    def is_leaf(self):
        """
        if this node is leaf node return 1 else return 0
        """
        return self._child_action == []

    def is_root(self):
        """
        if this node is root node return 1 else return 0
        """
        return self._parent_node is None

    def is_full_expended(self):
        """
        if this node is full expended(all possible moves have been calculated)
         return 1 else return 0)
        """
        if len(self._child_action) == len(self.move_list):
            return 1
        else:
            return 0


def my_MCTS_fun():
    """
    function in
    """
    testBoard = Board()  # initialization board
    node = TreeNode(0, None, [6, 3], testBoard)  # root node
    node.possible_moves()  # find all possible moves of root node
    node._reset_piece_location = node._state._player[node._turn][:2]
    # save note node's origin location
    i = 0  # set timeout!
    while(i < 1000):
        i = i + 1
#         print("i = ", i)
#         if i == 37:
#             print("end")
        while node.is_full_expended():   
            #  if all possible moves has been calculated
            #  select node begin with root node
            while not node.is_root():
                action = node._action
                node = node._parent_node  # located to root node
                node.reset_board(node._turn, node._reset_piece_location,
                                 action)  # reset noard
            while not node.is_leaf():  # select child node until leaf node
                action = node._state._player[1-node._turn][:2]
                node = node.UCT_select_child()
                node._reset_piece_location = action
            node.possible_moves()  # search possible moves for leaf node
        child_node = node.expend_child()  # expended child
        child_node._reset_piece_location = node._reset_piece_location
        value = child_node.simulation_()  # calculate board judge point
        child_node.update(value)  # update value
        child_node.reset_board(1-child_node._turn, child_node._reset_piece_location,
                               child_node._action)  # reset noard
    node = node.UCT_select_child()
    print(node._action)
#         node = TreeNode(None, [0, 3], testBoard)

"""
test Function in
"""
if __name__ == '__main__':
    my_MCTS_fun()
