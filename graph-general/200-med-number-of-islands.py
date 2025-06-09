# Leetcode 200: Number of Islands
# Link: https://leetcode.com/problems/number-of-islands/

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Solution using DFS approach
        Time Complexity: O(m*n) where m and n are dimensions of the grid
        Space Complexity: O(m*n) for the visited set and recursion stack
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def dfs(r, c):
            # Check if current position is valid and is land
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == "0" or 
                (r, c) in visited):
                return
            
            # Mark current cell as visited
            visited.add((r, c))
            
            # Explore all four directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left
        
        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        
        return islands
    
    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        """
        Solution using BFS approach
        Time Complexity: O(m*n) where m and n are dimensions of the grid
        Space Complexity: O(min(m,n)) for the queue
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            
            while queue:
                row, col = queue.popleft()
                
                # Check all four directions
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    
                    if (0 <= new_r < rows and 
                        0 <= new_c < cols and 
                        grid[new_r][new_c] == "1" and 
                        (new_r, new_c) not in visited):
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
        
        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
        
        return islands