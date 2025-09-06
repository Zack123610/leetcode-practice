# Leetcode 124: Binary Tree Maximum Path Sum
# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Post Order DFS
        maxPath = -float("inf")

        def gainFromSubtree(node):
            nonlocal maxPath

            if not node:
                return 0

            left = max(gainFromSubtree(node.left), 0)
            right = max(gainFromSubtree(node.right), 0)

            maxPath = max(maxPath, left + right + node.val)

            return max(left + node.val, right + node.val)
        
        gainFromSubtree(root)
        return maxPath