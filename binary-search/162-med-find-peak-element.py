# Leetcode 162: Find Peak Element
# Link: https://leetcode.com/problems/find-peak-element/

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return 
    
class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        def search(left, right):
            if left == right:
                return left
            
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return search(left, mid)
            return search(mid+1, right)

        return search(0, len(nums)-1)