# Leetcode 49: Group Anagrams
# Link: https://leetcode.com/problems/group-anagrams/

from typing import List
import collections

class Solution:
    '''
    Time Complexity: O(n * k)
    Space Complexity: O(n * k)
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())