# Leetcode 34: Find First and Last Position of Element in Sorted Array
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List

class Solution:
    '''
    Approach 1: Binary Search
    Time Complexity: O(log n)
    Space Complexity: O(1)
    '''
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        lower_bound = self.findBound(nums, target, True)
        if lower_bound == -1:
            return [-1, -1]

        upper_bound = self.findBound(nums, target, False)

        return [lower_bound, upper_bound]

    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:

        N = len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((begin + end) / 2)

            if nums[mid] == target:

                if isFirst:
                    # This means we found our lower bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    # Search on the left side for the bound.
                    end = mid - 1
                else:

                    # This means we found our upper bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid

                    # Search on the right side for the bound.
                    begin = mid + 1

            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1

        return -1
    
class Solution2:
    '''
    Approach 2: My Solution
    Time Complexity: O(log n)
    Space Complexity: O(1)
    '''
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1

        def findTarget(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        pos = findTarget(left, right)
        if pos == -1:
            return [-1, -1]
        
        def findStartEnd(pos):
            start, end = pos, pos
            # expand left
            while start > 0 and nums[start - 1] == target:
                start -= 1
            # expand right
            while end < len(nums) - 1 and nums[end + 1] == target:
                end += 1
            return [start, end]
         
        return findStartEnd(pos)
        