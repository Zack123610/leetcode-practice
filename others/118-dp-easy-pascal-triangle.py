# Leetcode 118: Pascal's Triangle
# Link: https://leetcode.com/problems/pascals-triangle/

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        
        dp = [[1]]  # first row

        for i in range(1, numRows):
            row = [1] * (i + 1)  # pre-size row with 1s
            for j in range(1, i):  # fill interior using previous row
                row[j] = dp[i - 1][j - 1] + dp[i - 1][j]
            dp.append(row)

        return dp