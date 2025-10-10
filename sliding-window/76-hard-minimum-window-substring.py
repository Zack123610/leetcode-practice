# Leetcode 76: Minimum Window Substring
# Link: https://leetcode.com/problems/minimum-window-substring/

from typing import List

class Solution:

    '''
    Time Complexity: O(∣S∣+∣T∣) where |S| and |T| represent the lengths of strings S and T.
    In the worst case we might end up visiting every element of string S twice, once by left pointer and once by right pointer. ∣T∣ represents the length of string T.

    Space Complexity: O(∣S∣+∣T∣). ∣S∣ when the window size is equal to the entire string S. ∣T∣ when T has all unique characters.
    '''
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not s or not t:
            return ""

        t_count = {}
        for ch in t:
            t_count[ch] = 1+ t_count.get(ch, 0)
        
        left, right = 0, 0
        have, need = 0, len(t_count)
        s_count = {}
        res = ""
        
        while right < len(s):

            s_count[s[right]] = 1 + s_count.get(s[right], 0)
           
            ch = s[right]
            if ch in t_count and s_count[ch] == t_count[ch]:
                have += 1

            # Left shift logic: # Try to shrink from the left while window is valid
            while have == need:

                # Update result if this window is smaller
                winLen = right - left + 1
                if not res or winLen < len(res):
                    res = s[left:right+1]

                # Update result if this window is smaller
                ch = s[left]
                s_count[ch] -= 1
                if ch in t_count and s_count[ch] < t_count[ch]:
                    have -= 1
                
                left += 1

            right += 1
        
        return res