# Leetcode 11: Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        left, right = 0, len(height)-1

        while left < right:

            water = (right-left) * min(height[left], height[right])
            maxWater = max(maxWater, water)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            
        return maxWater