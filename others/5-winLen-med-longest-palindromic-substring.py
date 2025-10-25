# Leetcode 5: Longest Palindromic Substring
# Link: https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    '''
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    '''
    def longestPalindrome(self, s: str) -> str:
        
        if not s or len(s) == 1:
            return s

        start = end = 0  # inclusive indices of best palindrome

        def expand(l: int, r: int) -> None:
            nonlocal start, end
            # expand while it's a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > (end - start + 1):
                    start, end = l, r
                l -= 1
                r += 1
            # when loop ends, [l, r] is the longest palindrome


        for i in range(len(s)):
            # odd length palindromes (center at i)
            expand(i, i)
            # even length palindromes (center between i and i+1)
            expand(i, i + 1)

        return s[start:end + 1]