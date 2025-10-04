# Leetcode 217: Contains Duplicates
# Link: https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


class Solution2:
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False


# Example usage
if __name__ == "__main__":
    solution = Solution()