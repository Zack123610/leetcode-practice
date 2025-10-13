# Leetcode 226: Invert Binary Tree
# Link: https://leetcode.com/problems/invert-binary-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Time Complexity: O(n)
    Space Complexity: O(h) h - height of the tree
    '''
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = right, left
    
        return root