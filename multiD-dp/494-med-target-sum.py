# Leetcode 494 - Target Sum
# https://leetcode.com/problems/target-sum/

from typing import List
from collections import defaultdict

class Solution:
    '''
    Time Complexity: O(n*m)
    Space Complexity: O(n*m)
    '''
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count

        return dp[n][target]

class SpaceOptimizedSolution:
    '''
    Time Complexity: O(n*m)
    Space Complexity: O(m)
    '''
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp

        return dp[target]