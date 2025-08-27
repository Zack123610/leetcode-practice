# Leetcode 3: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        res = 0

        for r in range(len(s)):
            # shrink window until s[r] is unique
            while s[r] in window:
                window.remove(s[left])   # or window.discard(s[left])
                left += 1

            window.add(s[r])
            res = max(res, r - left + 1)

        return res
        