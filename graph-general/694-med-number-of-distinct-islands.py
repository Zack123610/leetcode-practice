# Leetcode 694: Number of Distinct Islands
# Link: https://leetcode.com/problems/number-of-distinct-islands/

from typing import List

class Solution:
    '''
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    '''
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            
            if (row, col) in visited or grid[row][col] != 1:
                return
            
            visited.add((row, col))
            curr_island.add((row - row_origin, col - col_origin))

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        visited = set()
        unique_islands = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                curr_island = set()
                row_origin = row
                col_origin = col
                dfs(row, col)

                if curr_island:
                    unique_islands.add(frozenset(curr_island))
        
        return len(unique_islands)