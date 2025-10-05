# Leetcode 347: Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
import heapq
from typing import List

class Solution:
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # setup a hashmap counter
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # setup bucket
        freq = [ [] for i in range(len(nums) + 1)]
        for n, c, in count.items():
            freq[c].append(n)
        
        # Find most frequent num
        res = []
        for bucket in freq[::-1]:
            if bucket:
                for i in bucket:
                    res.append(i)
                    if len(res) == k:
                        return res
        
        return res

class Solution2:
    '''
    Using Heap
    Time Complexity: O(n log k)
    Space Complexity: O(n)
    '''
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        
        return heapq.nlargest(k, counter.keys(), key=counter.get)