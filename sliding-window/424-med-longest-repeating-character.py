# Leetcode 424: Longest Repeating Character Replacement
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/

from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:        
        hashmap = {}
        left, right = 0, 0
        res, maxf = 0, 0

        while right < len(s):

            hashmap[s[right]] = 1 + hashmap.get(s[right], 0)
            maxf = max(maxf, hashmap[s[right]])
            
            while (right - left + 1) - maxf > k:
                hashmap[s[left]] -= 1
                left += 1

            res = max(res, right-left+1)
            right += 1
        
        return res
        