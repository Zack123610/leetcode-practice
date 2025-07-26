# Leetcode 198: House Robber
# Link: https://leetcode.com/problems/house-robber/

from typing import List

class Solution:
    '''
    Approach 1: Dynamic Programming
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]
    
class Solution2:
    '''
    Approach 2: Dynamic Programming - Optimized
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev2, prev1 = 0, 0
        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
        
        return prev1