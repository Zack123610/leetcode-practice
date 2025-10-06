# Leetcode 387: First Unique Character in a String
# Link: https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1

class SolutionLeetcode:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map: character and how often it appears
        count = Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1

class SolutionSelf:
    def firstUniqChar(self, s: str) -> int:
        counter = {}

        for ch in s:
            counter[ch] = 1 + counter.get(ch, 0)

        # Sort according to value
        item = sorted(counter, key=counter.get)[0]
        if counter.get(item) != 1:
            return -1
        else:
            return s.index(item)
