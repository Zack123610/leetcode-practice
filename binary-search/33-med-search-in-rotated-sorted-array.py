# Leetcode 33: Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    '''
    Approach 1: Find Pivot Index + Binary Search
    Time Complexity: O(log n)
    Space Complexity: O(1)
    '''
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        # Find the index of the pivot element (the smallest element)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        # Binary search over an inclusive range [left_boundary ~ right_boundary]
        def binarySearch(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        # Binary search over elements on the pivot element's left
        if (answer := binarySearch(0, left - 1, target)) != -1:
            return answer

        # Binary search over elements on the pivot element's right
        return binarySearch(left, n - 1, target)
    
class Solution2:
    '''
    Approach 2: Find Pivot Index + Binary Search with Shift
    Time Complexity: O(log n)
    Space Complexity: O(1)
    '''
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        # Find the index of the pivot element (the smallest element)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        # Shift elements in circular manner, with the pivot element at index 0.
        # Then perform a regular binary search
        def shiftedBinarySearch(pivot_index, target):
            shift = n - pivot_index
            left, right = (pivot_index + shift) % n, (
                pivot_index - 1 + shift
            ) % n

            while left <= right:
                mid = (left + right) // 2
                if nums[(mid - shift) % n] == target:
                    return (mid - shift) % n
                elif nums[(mid - shift) % n] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        return shiftedBinarySearch(left, target)