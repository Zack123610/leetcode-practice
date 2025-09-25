# Leetcode 502: IPO
# Link: https://leetcode.com/problems/ipo/

from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Min-heap by required capital
        min_cap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_cap)

        # Max-heap for profits (store negatives)
        max_profit = []

        for _ in range(k):
            # Push all projects we can currently afford into the max-profit heap
            while min_cap and min_cap[0][0] <= w:
                c, p = heapq.heappop(min_cap)
                heapq.heappush(max_profit, -p)

            # If none are affordable, we're done
            if not max_profit:
                break

            # Choose the most profitable affordable project
            w += -heapq.heappop(max_profit)

        return w
