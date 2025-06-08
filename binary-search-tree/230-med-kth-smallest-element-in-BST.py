# Leetcode 230: Kth Smallest Element in a BST
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Solution 1: Iterative approach using stack
        stack = []
        current = root
        
        while True:
            # Reach the leftmost node of current node
            while current:
                stack.append(current)
                current = current.left
            
            # Process the node at the top of stack
            current = stack.pop()
            k -= 1
            
            # If we've found the kth smallest element
            if k == 0:
                return current.val
            
            # Move to the right subtree
            current = current.right

    def kthSmallest_recursive(self, root: TreeNode, k: int) -> int:
        # Solution 2: Recursive approach using inorder traversal
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        # Get all elements in sorted order and return the kth element
        return inorder(root)[k-1]