# Leetcode 129 - Med - Sum Root to Leaf Numbers
# Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # DFS Solution
        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum = current_sum * 10 + node.val
            
            if not node.left and not node.right:
                return current_sum
                
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        return dfs(root, 0)
    
    # Time Complexity: O(n) where n is the number of nodes
    # Space Complexity: O(n) where h is the height of the tree (due to recursion stack)
    
    def sumNumbersBFS(self, root: Optional[TreeNode]) -> int:
        # BFS Solution
        if not root:
            return 0
            
        total_sum = 0
        queue = [(root, 0)]
        
        while queue:
            node, current_sum = queue.pop(0)
            current_sum = current_sum * 10 + node.val
            
            if not node.left and not node.right:
                total_sum += current_sum
                continue
                
            if node.left:
                queue.append((node.left, current_sum))
            if node.right:
                queue.append((node.right, current_sum))
                
        return total_sum
    
    # Time Complexity: O(n) where n is the number of nodes
    # Space Complexity: O(n) where n is the number of nodes (due to queue), O(n) in the worst case (when the tree is a complete binary tree)

