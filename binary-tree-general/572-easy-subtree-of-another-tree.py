# Leetcode 572: Subtree of Another Tree
# Link: https://leetcode.com/problems/subtree-of-another-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Time complexity: O(m*n)
    Space complexity: O(m + n)
    Where m is the number of nodes in subRoot and n is the number of nodes in root.
    '''
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right