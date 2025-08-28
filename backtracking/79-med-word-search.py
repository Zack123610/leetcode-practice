# Leetcode 79: Word Search
# Link: https://leetcode.com/problems/word-search/

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r: int, c: int, pos: int) -> bool:
            # All characters matched
            if pos == len(word):
                return True

            # Out of bounds / mismatch / already used
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                board[r][c] != word[pos] or (r, c) in visited):
                return False

            visited.add((r, c))
            found = (
                dfs(r + 1, c, pos + 1) or
                dfs(r - 1, c, pos + 1) or
                dfs(r, c + 1, pos + 1) or
                dfs(r, c - 1, pos + 1)
            )
            visited.remove((r, c))  # backtrack
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

class OptimalBacktrackingSolution:
    '''
    Time Complexity: O(N⋅3^L)
    Space Complexity: O(L)
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False

    def backtrack(self, row: int, col: int, suffix: str) -> bool:
        """
        backtracking with side-effect,
           the matched letter in the board would be marked with "#".
        """
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if (
            row < 0
            or row == self.ROWS
            or col < 0
            or col == self.COLS
            or self.board[row][col] != suffix[0]
        ):
            return False

        # mark the choice before exploring further.
        self.board[row][col] = "#"
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            # sudden-death return, no cleanup.
            if self.backtrack(row + rowOffset, col + colOffset, suffix[1:]):
                return True

        # revert the marking
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return False