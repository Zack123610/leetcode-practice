# Leetcode 215: Kth Largest Element in an Array
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

class Solution2:
    '''
    Time Complexity: O(n log k)
    Space Complexity: O(k)
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]