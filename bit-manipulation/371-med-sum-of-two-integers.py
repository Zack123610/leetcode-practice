# Leetcode 371: Sum of Two Integers
# Link: https://leetcode.com/problems/sum-of-two-integers/

class Solution:
    '''
    Bit Manipulation
    Time Complexity: O(1)
    Space Complexity: O(1)
    '''
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while (b != 0):
            answer = a ^ b
            carry = (a & b) << 1
            a = answer & mask
            b = carry & mask
        
        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)