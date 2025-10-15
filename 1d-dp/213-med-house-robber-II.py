# Leetcode 213: House Robber II
# Link: https://leetcode.com/problems/house-robber-ii/

from typing import List

class SolutionSpaceOptimized:
    '''
    DP + Bottom-Up
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]),
                            self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

class Solution:
    '''
    DP + Bottom-Up
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
    
    def helper(self, houses):
        if len(houses) == 1:
            return houses[0]
        
        n = len(houses)
        dp = [0] * (n + 1)
        dp[1] = houses[0]

        for i in range(2, n+1):
            dp[i] = max(dp[i-1], houses[i-1] + dp[i-2])
        
        return dp[-1]