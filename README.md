# leetcode-practice

## Tips

### Merge Sort

Here's how the algorithm works:
1. **Base Case**: If the list is empty or has only one node, return it as is.
2. **Divide**:
- Use the "slow and fast pointer" technique to find the middle of the list
- Split the list into two halves at the middle point
3. **Conquer**:
Recursively sort both halves of the list
4. **Combine**:
- Merge the sorted halves using the `merge` method
- Sorting logic happens here inside the `merge` method
- The merge method uses a dummy node to handle the merging process efficiently

**Time Complexity**: O(n log n)
**Space Complexity**: O(log n) due to the recursion stack

Relevant Leetcode Questions:
- Leetcode 148: Sort List

### 1-Dimension Dynamic Programming
1. The problem asks for the number of distinct ways to climb n stairs when you can take either 1 or 2 steps at a time.
2. For small inputs (n ≤ 2), we return n directly:
- For n=1: Only 1 way (take one 1-step)
- For n=2: 2 ways (two 1-steps or one 2-step)
3. For larger inputs, we use a bottom-up DP approach:
- Create a dp array where dp[i] = number of ways to climb i stairs
- Set base cases: dp[1] = 1 and dp[2] = 2
- For each stair i from 3 to n, the number of ways equals:

dp[i] = dp[i-1] + dp[i-2]

This is because you can reach stair i by:
- Taking 1 step from stair i-1
- Taking 2 steps from stair i-2
4. The final answer is dp[n].

This follows the Fibonacci sequence pattern, with time complexity O(n) and space complexity O(n).

Relevant Leetcode Questions:
- Leetcode 70: Climbing Stairs

### Multi-D Dynamic Programming

1. We create a 2D DP array of size (m+1) x (n+1) where m and n are the lengths of text1 and text2 respectively. The extra row and column are for the base case where one of the strings is empty.
2. We iterate through both strings using nested loops:
- If the current characters match (text1[i-1] == text2[j-1]), we take the diagonal value (dp[i-1][j-1]) and add 1 to it
- If they don't match, we take the maximum of the left cell (dp[i][j-1]) and top cell (dp[i-1][j])
3. The final answer is stored in dp[m][n], which represents the length of the longest common subsequence between the entire text1 and text2.

**Time complexity** is O(mn) where m and n are the lengths of the input strings<br>
**Space complexity** is also O(mn) for the DP table.


Relevant Leetcode Questions:
- Leetcode 1143: Longest Common Sequence