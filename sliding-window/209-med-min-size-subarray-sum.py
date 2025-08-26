# Leetcode 209: Minimum Size Subarray Sum
# Link: https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        windowSum = 0
        minSize = float('inf')

        for r in range(len(nums)):
            windowSum += nums[r]

            # shrink while the window meets/exceeds target
            while windowSum >= target:
                minSize = min(minSize, r - left + 1)
                windowSum -= nums[left]  # subtract the element leaving the window
                left += 1                # then move left

        return 0 if minSize == float('inf') else minSize

    
