# Leetcode 72: Edit Distance
# Link: https://leetcode.com/problems/edit-distance/

from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1, w2 = len(word1), len(word2)

        # Correct base cases (or just rely on dp initialization)
        if w1 == 0:
            return w2
        if w2 == 0:
            return w1

        dp = [[0] * (w2 + 1) for _ in range(w1 + 1)]

        for i in range(1, w1 + 1):
            dp[i][0] = i
        for j in range(1, w2 + 1):
            dp[0][j] = j

        for i in range(1, w1 + 1):
            for j in range(1, w2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],     # delete
                        dp[i][j - 1],     # insert
                        dp[i - 1][j - 1]  # replace
                    )

        return dp[w1][w2]