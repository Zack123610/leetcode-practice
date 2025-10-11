# Leetcode 191: Number of 1 Bits
# Link: https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

class Solution2:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        
        return res