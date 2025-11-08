# Leetcode 274: H-Index
# Link: https://leetcode.com/problems/h-index/

from typing import List

class Solution:
    '''
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    '''
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0

class SortingSolution:
    '''
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    '''
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        i = 0
        while i < len(citations) and citations[len(citations)-1-i] > i:
            i += 1
        return i

class CountingSolution:
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n + 1)
        for citation in citations:
            if citation >= n:
                count[n] += 1
            else:
                count[citation] += 1
        for i in range(n, -1, -1):
            if count[i] >= i:
                return i
        return 0