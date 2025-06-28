# Leetcode 918: Maximum Sum Circular Subarray
# Link: https://leetcode.com/problems/maximum-sum-circular-subarray/

from typing import List

class Solution:
    # Calculate the "Minimum Subarray"
    '''
    Complexity Analysis
    Here, N is the length of the input array.

    Time complexity: O(N).
    The algorithm iterates over all elements to calculate the maxSum, minSum, and sum which takes O(N) time.

    Space complexity: O(1).
    '''
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
        