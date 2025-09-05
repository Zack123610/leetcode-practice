# Leetcode 99: Recover Binary Search Tree
# Link: https://leetcode.com/problems/recover-binary-search-tree/

from typing import Optional

'''
Time Complexity: O(n)
Space Complexity: O(h)
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        curr = root
        prev = None
        x = y = None

        while stack or curr:
            # Go to leftmost
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Detect inversions in inorder sequence
            if prev and curr.val < prev.val:
                y = curr
                if x is None:
                    x = prev
                else:
                    # Found both, can stop early
                    break

            prev = curr
            curr = curr.right

        # Swap values of the two nodes
        if x and y:
            x.val, y.val = y.val, x.val
