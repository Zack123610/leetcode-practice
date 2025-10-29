# Leetcode 268: Missing Number
# Link: https://leetcode.com/problems/missing-number/

from typing import List

class MySolution:
    def missingNumber(self, nums: List[int]) -> int:
        hashset = set(nums)
        n = len(nums)

        for i in range(n+1):
            if i not in hashset:
                return i

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)