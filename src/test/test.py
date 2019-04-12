'''
Created on 2019年3月27日

@author: Martha Zhao
'''
from math import sqrt, log
from random import choice
import psutil
import os

class Node():
    def __init__(self, w, v, parent):
        self._w = w
        self._v = v
        self.parent = parent
        self._childNodes = []

    def UCTSelectChild(self):
        """ Use the UCB1 formula to select a child node.
            Often a constant UCTK is applied so we have
            lambda c: c.wins/c.visits + UCTK * sqrt(2*log(self.visits)/c.visits
            to vary the amount of
            exploration versus exploitation.
        """
        s = sorted(self._childNodes,
                   key=lambda c: c._w/c._v +
                   sqrt(2*log(self._v)/c._v),
                   reverse=True)
#         for it in s:
#             str_ = 's-w = ' + str(it._w) + ' s_v = ' + str(it._v)
#             print(str_)
        str_ = 's-w = ' + str(s[0]._w) + ' s_v = ' + str(s[0]._v)
        print(str_)
        return s[0]

    def add_child(self, child):
        self._childNodes.append(child)


if __name__ == '__main__':

    a = [1, 2, 3, 4, 5]
    b = choice(a)
    print(b)
    
    a = None
    if a is not None:
        print ('not None')
    else:
        print ('None')
    info = psutil.virtual_memory()
    print('内存使用：', psutil.Process(os.getpid()).memory_info().rss)
    print('总内存：',info.total)
    print('内存占比：',info.percent)