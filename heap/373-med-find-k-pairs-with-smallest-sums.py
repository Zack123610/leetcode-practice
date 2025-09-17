# Leetcode 373: Find K Pairs with Smallest Sums
# Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)

        ans = []
        visited = set()

        minHeap = [ (nums1[0]+nums2[0], (0, 0))]
        visited.add((0, 0))

        while k > 0 and minHeap:
            val, (i, j) = heapq.heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            if i+1 < m and (i+1, j) not in visited:
                heapq.heappush(minHeap, (nums1[i+1] + nums2[j], (i+1, j)))
                visited.add((i+1, j))
            
            if j+1 < n and (i, j+1) not in visited:
                heapq.heappush(minHeap, (nums1[i] + nums2[j+1], (i, j+1)))
                visited.add((i, j+1))

            k -= 1
        
        return ans

class optimalSolution:

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        if m == 0 or n == 0 or k == 0:
            return []

        ans: List[List[int]] = []
        minHeap = []

        # Start with the smallest element in each row: (sum, i, j)
        for i in range(min(m, k)):
            heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))

        while k > 0 and minHeap:
            _, i, j = heapq.heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            if j + 1 < n:  # push next element in the same row
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))

            k -= 1

        return ans