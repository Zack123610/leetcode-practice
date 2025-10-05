# Leetcode 37: Sudoku Solver
# Link: https://leetcode.com/problems/sudoku-solver/

from typing import List
import collections

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key: (r//3, c//3)

        # Seed the constraint sets
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    squares[(r // 3, c // 3)].add(num)

        def backtracking(r: int, c: int) -> bool:
            # If we've filled past the last row, we're done
            if r == 9:
                return True

            # Compute next cell coordinates
            nr, nc = (r, c + 1) if c < 8 else (r + 1, 0)

            # Skip filled cells
            if board[r][c] != ".":
                return backtracking(nr, nc)

            # Try digits 1..9
            for ch in "123456789":
                if ch in rows[r] or ch in cols[c] or ch in squares[(r//3, c//3)]:
                    continue

                # Place
                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                squares[(r // 3, c // 3)].add(ch)

                # Recurse
                if backtracking(nr, nc):
                    return True

                # Undo
                board[r][c] = "."
                rows[r].remove(ch)
                cols[c].remove(ch)
                squares[(r // 3, c // 3)].remove(ch)

            # No valid digit worked here
            return False

        backtracking(0, 0)
