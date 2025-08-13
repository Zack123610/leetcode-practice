# Leetcode 300 - Longest Increasing Subsequence
# Link: https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] is the length of the longest increasing subsequence that ends with nums[i]
        # dp[i] = max(dp[j] + 1) for all j < i and nums[j] < nums[i]
        # initialize dp with 1s

        if not nums:
            return 0

        # Bottom up DP
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# Test cases
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solution().lengthOfLIS(nums))