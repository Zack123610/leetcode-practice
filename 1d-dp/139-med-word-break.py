# Leetcode 139: Word Break
# Link: https://leetcode.com/problems/word-break/

from typing import List

class mySolution:
    '''
    Approach 1: Dynamic Programming
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Initialize DP array
        dp = [False] * len(s)

        # For loop
        for i in range(len(s)):
            for word in wordDict:
                # Handle out of bounds case
                if i < len(word) - 1:
                    continue
                
                if i == len(word)-1 or dp[ i - len(word) ]:
                    # check string matching
                    if s[i+1 - len(word) : i+1] == word:
                        dp[i] = True
                        break
        
        return dp[-1]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word) and s[i-len(word):i] == word:
                    dp[i] = dp[i] or dp[i-len(word)]
        
        return dp[-1]
    
class Solution2:
    '''
    Approach 2: Dynamic Programming - Optimized
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word) and s[i-len(word):i] == word:
                    dp[i] = dp[i] or dp[i-len(word)]
        
        return dp[-1]