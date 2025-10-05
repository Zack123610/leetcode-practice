# Leetcode 36: Valid Sudoku
# Link: https://leetcode.com/problems/valid-sudoku/

import collections
from typing import List

class Solution:
    '''
    Time Complexity: O(N^2)
    Space Complexity: O(N^2)
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3,c // 3)]):
                    return False
        
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3,c // 3)].add(board[r][c])

        return True