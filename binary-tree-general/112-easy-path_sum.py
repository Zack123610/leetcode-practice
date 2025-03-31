from typing import Optional

# Leetcode 112: Path Sum
# Link: https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: if root is None, return False
        if not root:
            return False
        
        # If we reach a leaf node, check if remaining sum equals node value
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursively check left and right subtrees with reduced target sum
        remaining = targetSum - root.val
        return (self.hasPathSum(root.left, remaining) or 
                self.hasPathSum(root.right, remaining))

# Example usage:
# Constructing a binary tree:
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1

# Target sum = 22
