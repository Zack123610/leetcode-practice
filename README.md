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