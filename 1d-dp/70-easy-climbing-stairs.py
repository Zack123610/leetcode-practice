# Leetcode 70: Climbing Stairs
# Link: https://leetcode.com/problems/climbing-stairs/

class Solution:
    '''
    DP + Bottom-Up
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n <= 2:
            return n
        
        # Initialize dp array
        dp = [0] * (n + 1)
        dp[1] = 1  # One way to climb 1 step
        dp[2] = 2  # Two ways to climb 2 steps (1+1 or 2)
        
        # Fill dp array
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]

# This follows the Fibonacci sequence pattern, with time complexity O(n) and space complexity O(n).

# We can optimize the space complexity to O(1) by using two variables to store the last two values instead of an array.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev, curr = 1, 2
        
        for i in range(3, n + 1):
            prev, curr = curr, prev + curr
            
        return curr

# This follows the Fibonacci sequence pattern, with time complexity O(n) and space complexity O(1).

