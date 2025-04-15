# Leetcode 167: Two Sum II - Input Array Is Sorted
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # 1-based indexing
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
        return [-1, -1]  # This line is technically not needed as per problem constraints

