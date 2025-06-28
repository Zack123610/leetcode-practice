# Leetcode 918: Maximum Sum Circular Subarray
# Link: https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = curMin = 0
        maxSum = minSum = nums[0]
        totalSum = 0

        for i in range(len(nums)):
            curMax = max(curMax, 0) + nums[i]
            maxSum = max(maxSum, curMax)

            curMin = min(curMin, 0) + nums[i]
            minSum = min(minSum, curMin)

            totalSum += nums[i]
        
        # Special case
        if totalSum == minSum:
            return maxSum

        return max(maxSum, totalSum - minSum)
        