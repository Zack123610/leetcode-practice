# Leetcode 1: Two Sum
# Link: https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers
        such that they add up to target.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices whose values sum to target
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Create a dictionary to store value-index pairs
        num_map = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach target
            complement = target - num
            
            # If complement exists in the map, return the indices
            if complement in num_map:
                return [num_map[complement], i]
            
            # Store the current number and its index
            num_map[num] = i
        
        # No solution found (though problem states there is exactly one solution)
        return []

    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force solution for Two Sum problem.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(solution.twoSum(nums1, target1))  # Output: [0, 1]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(solution.twoSum(nums2, target2))  # Output: [1, 2]
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(solution.twoSum(nums3, target3))  # Output: [0, 1]
