# Leetcode 994: Rotting Oranges
# Link: https://leetcode.com/problems/rotting-oranges/

from typing import Any, List
from collections import deque

class MySolution:
    '''
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque[Any]([])
        fresh = 0
        minutes = 0

        def bfs():
            nonlocal fresh, minutes
            while q and fresh > 0:

                qLen = len(q)

                for _ in range(qLen):
                    r, c = q.popleft()

                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                    for dr, dc in directions:
                        new_r = r + dr
                        new_c = c + dc

                        if new_r < ROWS and new_r >= 0 and new_c < COLS and new_c >= 0 and grid[new_r][new_c] == 1:
                            grid[new_r][new_c] = 2
                            fresh -= 1
                            q.append((new_r, new_c))
                
                minutes += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        else:
            bfs()

        return minutes if fresh == 0 else -1    