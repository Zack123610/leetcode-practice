# Leetcode 128: Longest Consecutive Sequence
# Link: https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1 

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                    
                longest = max(longest, current_streak)
                
        return longest