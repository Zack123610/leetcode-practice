# Leetcode 78: Subsets
# Link: https://leetcode.com/problems/subsets/

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(index: int, curr: List[int]):
            # Add a copy of the current subset
            res.append(curr.copy())

            # Generate subsets starting from 'index'
            for i in range(index, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        # Call backtrack starting from 0 with empty subset
        backtrack(0, [])
        return res
