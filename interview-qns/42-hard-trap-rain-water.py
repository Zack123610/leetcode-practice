# Leetcode 42: Trapping Rain Water
# Link: https://leetcode.com/problems/trapping-rain-water/

from typing import List


class selfSolution:
    def trap(self, height: List[int]) -> int:
        # consts
        ans = 0
        size = len(height)
        maxleft_dp = [0] * size
        maxright_dp = [0] * size

        maxleft_dp[0] = height[0]
        for i in range(1, size):
            maxleft_dp[i] = max(height[i], maxleft_dp[i - 1])

        maxright_dp[-1] = height[-1]
        for i in range(size-2, -1, -1):
            maxright_dp[i] = max(height[i], maxright_dp[i+1])

        for i in range(1, size-1):
            ans += min(maxleft_dp[i], maxright_dp[i]) - height[i]
        
        return ans

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        ans = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
        
        return ans

