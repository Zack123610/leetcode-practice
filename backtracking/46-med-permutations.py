# Leetcode 46: Permutations
# Link: https://leetcode.com/problems/permutations/

from typing import List

class SolutionLeetcode:
    '''
    Time Complexity: O(n * n!)
    Space Complexity: O(n)
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
        
        res = []
        backtrack([])
        return res

class Solution:
    '''
    Time Complexity: O(n⋅n!)
    Space Complexity: O(n)
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []
        visited = set()
        
        def backtrack(curr: List[int]) -> None:
            if len(curr) == len(nums):
                ans.append(curr.copy())  # copy the current permutation
                return
            
            for num in nums:
                if num in visited:       # only use unused numbers
                    continue
                visited.add(num)
                curr.append(num)
                backtrack(curr)
                curr.pop()               # pop the last element
                visited.remove(num)
        
        backtrack([])
        return ans
