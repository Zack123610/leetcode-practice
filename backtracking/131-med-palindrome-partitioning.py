# Leetcode 131: Palindrome Partitioning
# Link: https://leetcode.com/problems/palindrome-partitioning/

from typing import List

class Solution:
    '''
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n)
    O(n * 2^n) space for the output list.
    '''
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isValidPalindrome(s):
            start, end = 0, len(s)-1
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def backtrack(start, curr):

            # if we've consumed the whole string, record the current partition
            if start == len(s):
                res.append(curr.copy())
                return
            
            for end in range(start, len(s)):

                # try all end positions; only recurse on palindromic slices
                if isValidPalindrome(s[start:end+1]):
                    curr.append(s[start:end+1])
                    backtrack(end+1, curr)
                    curr.pop()
        
        backtrack(0, [])
        return res
