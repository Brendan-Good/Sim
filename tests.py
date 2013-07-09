#!/usr/bin/env python3

import unittest
from negamax import *

class TestConnectFour(unittest.TestCase):
    def test_col(self):
        board = new_board()
        board = expand(board, 1)[0]
        board = expand(board, 1)[0]
        board = expand(board, 1)[0]
        board = expand(board, 1)[0]
        self.assertTrue(check_col(board, 0, 0))
        
    def test_col2(self):
        board = new_board()
        board = expand(board, 1)[0]
        board = expand(board, -1)[0]
        board = expand(board, 1)[0]
        board = expand(board, -1)[0]
        board = expand(board, -1)[0]
        board = expand(board, -1)[0]
        self.assertFalse(check_col(board, 0, 3))
        
    def test_col3(self):
        board = new_board()
        board = expand(board, 1)[0]
        board = expand(board, -1)[0]
        board = expand(board, -1)[0]
        board = expand(board, -1)[0]
        board = expand(board, -1)[0]
        board = expand(board, -1)[0]
        self.assertFalse(check_col(board, 0, 3))
        
    def test_terminal_slash(self):
        board = [[0,0,0,0,0,0], [1,0,0,0,0,0], [0,1,0,0,0,0], [0,0,1,0,0,0], [0,0,0,1,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
        self.assertTrue(is_terminal(board))
        
    def test_backslash(self):
        board = [[0,0,0,0,1,0], [0,0,0,1,0,0], [0,0,1,0,0,0], [0,1,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
        self.assertTrue(is_terminal(board))
        
if __name__ == '__main__':
    unittest.main()