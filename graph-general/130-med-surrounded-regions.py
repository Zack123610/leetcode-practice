# Leetcode 130: Surrounded Regions
# Link: https://leetcode.com/problems/surrounded-regions/

# Solution 1: DFS approach
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return

            board[r][c] = "T"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # DFS, capture unsurrounded regions -> T
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and ((r in [0, rows-1]) or (c in [0, cols-1])):
                    dfs(r, c)

        # Capture surrounded regions -> X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Uncapture unsurrounded regions -> O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        