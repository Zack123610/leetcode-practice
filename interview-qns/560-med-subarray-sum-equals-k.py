# Leetcode 560: Subarray Sum Equals K
# Link: https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List

class Solution:
    '''
    This is a prefix sum method to solve the problem.
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSum = { 0 : 1}

        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefixSum.get(diff, 0)

            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        
        return res