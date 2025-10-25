# Leetcode 63: Unique Paths II
# Link: https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        '''
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        # If start is blocked, no paths.
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = 1  # start

        # First row
        for c in range(1, cols):
            dp[0][c] = 0 if obstacleGrid[0][c] == 1 else dp[0][c - 1]

        # First column
        for r in range(1, rows):
            dp[r][0] = 0 if obstacleGrid[r][0] == 1 else dp[r - 1][0]

        # Rest of the grid
        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[rows - 1][cols - 1]