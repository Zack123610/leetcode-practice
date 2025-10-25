# Leetcode 123: Best Time to Buy and Sell Stock III
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

from typing import List

class SolutionLeetcode:
    '''
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = float("inf"), float("inf")
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit

class Solution:
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def maxProfit(self, prices: List[int]) -> int:
        
        # Initialize DP
        n = len(prices)

        left_profit = [0] * (n)
        right_profit = [0] * (n+1)


        # Loop through
        left_min = prices[0]
        right_max = prices[-1]
        l = 0

        for i in range(1, n):
            
            left_profit[i] = max(left_profit[i-1], prices[i] - left_min)
            left_min = min(left_min, prices[i])

            right = n - 1 - i
            right_profit[right] = max(right_profit[right+1], right_max - prices[right])
            right_max = max(right_max, prices[right])

        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, left_profit[i] + right_profit[i+1])
        
        return max_profit