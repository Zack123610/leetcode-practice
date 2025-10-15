# Leetcode 338: Counting Bits
# Link: https://leetcode.com/problems/counting-bits/

from typing import List

class Solution:
    '''
    DP + Last Set Bit
    Time Complexity: O(n)
    Space Complexity: O(1). Since the output array does not count towards the space complexity.
    '''
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans