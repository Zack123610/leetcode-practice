# Leetcode 417: Pacific Atlantic Water Flow
# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import List
from collections import deque

class Solution:
    '''
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    '''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights:
            return []
        
        ROWS, COLS = len(heights), len(heights[0])

        pacific_queue = deque()
        atlantic_queue = deque()
        
        for i in range(ROWS):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, COLS-1))
        
        for j in range(COLS):
            pacific_queue.append((0, j))
            atlantic_queue.append((ROWS-1, j))

        def bfs(queue):
            reachable = set()

            while queue:

                r, c = queue.popleft()
                reachable.add((r, c))

                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for dr, dc in dirs:
                    new_r, new_c = r + dr, c + dc
                
                    if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS:
                        continue
                    
                    # Check that new cell has not been visited
                    if (new_r, new_c) in reachable:
                        continue

                    # Check that the new cell has higher or equal height
                    if heights[new_r][new_c] < heights[r][c]:
                        continue
                    
                    queue.append((new_r, new_c))
            
            return reachable
        
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
    
        return list(pacific_reachable.intersection(atlantic_reachable))