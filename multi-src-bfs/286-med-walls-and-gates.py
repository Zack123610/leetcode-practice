# Leetcode 286: Walls and Gates
# Link: https://leetcode.com/problems/walls-and-gates/

from typing import Any, List
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        q = deque[Any]([])
        INF = 2 ** 31 -1

        def bfs():
            depth = 1
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:

                qLen = len(q)
                
                for _ in range(qLen):
                    r, c = q.popleft()
                    
                    for dr, dc in directions:
                        new_r = r + dr
                        new_c = c + dc

                        if new_r < ROWS and new_r >= 0 and new_c < COLS and new_c >= 0 and rooms[new_r][new_c] == INF:
                            rooms[new_r][new_c] = depth
                            q.append((new_r, new_c))
                    
                depth += 1

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))
        
        bfs()