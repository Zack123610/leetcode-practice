# Leetcode 912: Sort an Array
# Link: https://leetcode.com/problems/sort-an-array/

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Main method to sort the array.
        We'll implement both Quick Sort and Merge Sort.
        """
        # Choose which sorting algorithm to use
        # return self.quickSort(nums.copy())  # Uncomment for Quick Sort
        return self.mergeSort(nums.copy())    # Uncomment for Merge Sort
    
    def quickSort(self, nums: List[int]) -> List[int]:
        """
        Quick Sort Implementation
        Time Complexity: O(n log n) average, O(n²) worst case
        Space Complexity: O(log n) due to recursion stack
        """
        if len(nums) <= 1:
            return nums
        
        # Choose pivot (middle element to avoid worst case on sorted arrays)
        pivot = nums[len(nums) // 2]
        
        # Partition into three parts: less than, equal to, greater than pivot
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        
        # Recursively sort left and right parts, then combine
        return self.quickSort(left) + middle + self.quickSort(right)
    
    def mergeSort(self, nums: List[int]) -> List[int]:
        """
        Merge Sort Implementation
        Time Complexity: O(n log n) guaranteed
        Space Complexity: O(n) for temporary arrays
        """
        if len(nums) <= 1:
            return nums
        
        # Divide: split array into two halves
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        
        # Conquer: merge the sorted halves
        return self.merge(left, right)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        """
        Helper method to merge two sorted arrays
        """
        result = []
        i = j = 0
        
        # Compare elements from both arrays and merge in sorted order
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Add remaining elements from left array
        result.extend(left[i:])
        
        # Add remaining elements from right array
        result.extend(right[j:])
        
        return result


# Alternative in-place Quick Sort implementation (more memory efficient)
class SolutionInPlace:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        In-place Quick Sort implementation
        Time Complexity: O(n log n) average, O(n²) worst case
        Space Complexity: O(log n) due to recursion stack
        """
        self.quickSortInPlace(nums, 0, len(nums) - 1)
        return nums
    
    def quickSortInPlace(self, nums: List[int], left: int, right: int):
        """
        In-place Quick Sort with Lomuto partition scheme
        """
        if left >= right:           # <-- base case
            return
        
        # Partition the array and get pivot index
        pivot_index = self.partition(nums, left, right)
        
        # Recursively sort elements before and after pivot
        self.quickSortInPlace(nums, left, pivot_index - 1)
        self.quickSortInPlace(nums, pivot_index + 1, right)
    
    def partition(self, nums: List[int], left: int, right: int) -> int:
        """
        Lomuto partition scheme
        """
        # Choose the rightmost element as pivot
        pivot = nums[right]
        i = left - 1  # Index of smaller element
        
        # Move all elements smaller than pivot to the left
        for j in range(left, right):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        # Place pivot in its correct position
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1


# Test cases
if __name__ == "__main__":
    # Test the sorting algorithms
    test_cases = [
        [5, 2, 3, 1],
        [5, 1, 1, 2, 0, 0],
        [1],
        [],
        [3, 2, 1],
        [1, 2, 3],
        [1, 1, 1, 1]
    ]
    
    solution = Solution()
    solution_inplace = SolutionInPlace()
    
    print("Testing Merge Sort:")
    for nums in test_cases:
        sorted_nums = solution.sortArray(nums.copy())
        print(f"Input: {nums} -> Output: {sorted_nums}")
    
    print("\nTesting In-place Quick Sort:")
    for nums in test_cases:
        sorted_nums = solution_inplace.sortArray(nums.copy())
        print(f"Input: {nums} -> Output: {sorted_nums}")

