# Leetcode 47: Permutations II
# Link: https://leetcode.com/problems/permutations-ii/

from typing import List
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        counter = Counter(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                # make a deep copy of the resulting permutation
                ans.append(curr.copy())
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    curr.append(num)
                    counter[num] -= 1

                    # continue the exploration
                    backtrack(curr)

                    # revert the choice for the next exploration
                    curr.pop()
                    counter[num] += 1

        backtrack([])
        return ans