# Leetcode 74: Search a 2D Matrix
# Link: https://leetcode.com/problems/search-a-2d-matrix/

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows and columns in the matrix
        rows, cols = len(matrix), len(matrix[0])
        
        # Set the left and right boundaries
        left, right = 0, rows * cols - 1
        
        # While the left boundary is less than the right boundary
        while left <= right:
            # Get the middle index and the middle value
            mid = (left + right) // 2
            mid_val = matrix[mid // cols][mid % cols]
            
            # If the middle value is the target, return True
            if mid_val == target:
                return True
            # If the middle value is less than the target, discard the smaller half
            elif mid_val < target:
                left = mid + 1
            # If the middle value is greater than the target, discard the larger half
            else:
                right = mid - 1
        # If we finish the search without finding target, return False
        return False