# Leetcode 295: Find Median from Data Stream
# Link: https://leetcode.com/problems/find-median-from-data-stream/

from typing import List
import heapq

class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []
        

    def addNum(self, num: int) -> None:
        
        # Add num to lower half
        heapq.heappush(self.low, -num)

        # Maintain order: every item in low <= every item in high
        if self.high and (-self.low[0] > self.high[0]):
            val = heapq.heappop(self.low)
            heapq.heappush(self.high, -val)

        # Balance size: (low can have at most 1 more than high)
        if len(self.low) > len(self.high) + 1:
            val = heapq.heappop(self.low)
            heapq.heappush(self.high, -val)
        if len(self.high) > len(self.low):
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)  

    def findMedian(self) -> float:
        total = len(self.low) + len(self.high)

        if total % 2 == 1:
            mid = -self.low[0]
        else:
            mid = (-self.low[0] + self.high[0]) / 2
        
        return mid