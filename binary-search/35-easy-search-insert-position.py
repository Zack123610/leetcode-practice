# Leetcode 35: Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        Solution 1: Binary Search (Optimal)
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left
    
    def searchInsert_linear(self, nums: list[int], target: int) -> int:
        """
        Solution 2: Linear Search
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)
    
    def searchInsert_builtin(self, nums: list[int], target: int) -> int:
        """
        Solution 3: Using bisect module
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        import bisect
        return bisect.bisect_left(nums, target)
    
    def searchInsert_recursive(self, nums: list[int], target: int) -> int:
        """
        Solution 4: Recursive Binary Search
        Time Complexity: O(log n)
        Space Complexity: O(log n) due to recursion stack
        """
        def binary_search(left, right):
            if left >= right:
                return left
            
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left, mid)
        
        return binary_search(0, len(nums))


# Test cases
def test_solutions():
    solution = Solution()
    
    # Test case 1: Target exists in array
    nums1 = [1, 3, 5, 6]
    target1 = 5
    print(f"Test 1: nums={nums1}, target={target1}")
    print(f"Expected: 2, Got: {solution.searchInsert(nums1, target1)}")
    
    # Test case 2: Target should be inserted
    nums2 = [1, 3, 5, 6]
    target2 = 2
    print(f"Test 2: nums={nums2}, target={target2}")
    print(f"Expected: 1, Got: {solution.searchInsert(nums2, target2)}")
    
    # Test case 3: Target should be inserted at end
    nums3 = [1, 3, 5, 6]
    target3 = 7
    print(f"Test 3: nums={nums3}, target={target3}")
    print(f"Expected: 4, Got: {solution.searchInsert(nums3, target3)}")
    
    # Test case 4: Target should be inserted at beginning
    nums4 = [1, 3, 5, 6]
    target4 = 0
    print(f"Test 4: nums={nums4}, target={target4}")
    print(f"Expected: 0, Got: {solution.searchInsert(nums4, target4)}")
    
    # Test case 5: Empty array
    nums5 = []
    target5 = 1
    print(f"Test 5: nums={nums5}, target={target5}")
    print(f"Expected: 0, Got: {solution.searchInsert(nums5, target5)}")

if __name__ == "__main__":
    test_solutions()

