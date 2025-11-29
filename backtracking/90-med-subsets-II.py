# Leetcode 90: Subsets II
# Link: https://leetcode.com/problems/subsets-ii/

from typing import List

class Solution:
    '''
    Time Complexity: O(n * 2^n)
    the total number of recursive function calls will be 2^n
    Copying of the current subset takes (n) time.
    
    Space Complexity: O(n)
    The recursion call stack occupies at most O(n) space. 
    The output list of subsets is not considered while analyzing space complexity. 
    So, the space complexity of this approach is O(n)
    '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res: List[List[int]] = []

        def backtrack(start: int, curr: List[int]) -> None:
            res.append(curr.copy())
            for i in range(start, len(nums)):
                # skip duplicates at the same recursion depth
                if i > start and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])
        return res
