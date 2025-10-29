# Leetcode 190: Reverse Bits
# Link: https://leetcode.com/problems/reverse-bits/

class MySolution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res + (bit << (31 - i))
        return res

class Solution:
    '''
    Bit Manipulation
    Time Complexity: O(1)
    Space Complexity: O(1)
    '''
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)