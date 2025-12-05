# Leetcode 746 - Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # The array's length should be 1 longer than the length of cost
        # This is because we can treat the "top floor" as a step to reach
        dp = [ 0 ] * (len(cost)+1)

        # Start iteration from step 2, since the minimum cost of reaching
        # step 0 and step 1 is 0
        for i in range(2, len(cost)+1):
            dp[i] = min( dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        
        # The final element in minimum_cost refers to the top floor
        return dp[-1]