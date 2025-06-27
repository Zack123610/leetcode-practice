# Leetcode 53: Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/


from typing import List

# Kadane's Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation: We use a greedy approach to find the maximum sum of a contiguous subarray. We keep track of the current sum and the maximum sum encountered so far. If the current sum is negative, we reset it to 0. This is because a negative sum will only decrease the sum of a contiguous subarray.
# Example:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum