# Leetcode 153: Find Minimum in Rotated Sorted Array
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

class Solution:
    '''
    Approach 1: Binary Search - My Solution
    Time Complexity: O(log n)
    Space Complexity: O(1)
    '''
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:               
                left = mid + 1
            else:
                right = mid - 1
        
        return nums[left]
    
class Solution2:
    '''
    Approach 2: Leetcode Solution
    Time Complexity: O(log n)
    Space Complexity: O(1)
    '''
    def findMin(self, nums: List[int]) -> int:
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]

        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1

        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[right] > nums[0]:
            return nums[0]

        # Binary search way
        while right >= left:
            # Find the mid element
            mid = left + (right - left) // 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1
