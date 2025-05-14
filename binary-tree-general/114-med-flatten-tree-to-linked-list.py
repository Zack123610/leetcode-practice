# Leetcode 114: Flatten Binary Tree to Linked List
# Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Approach 1: Recursive Solution
        # Time Complexity: O(n)
        # Space Complexity: O(h) where h is the height of the tree (due to recursion stack)
        
        def flatten_tree(node):
            if not node:
                return None
            
            # Store the right subtree
            right_subtree = node.right
            
            # Flatten left subtree
            if node.left:
                node.right = node.left
                node.left = None
                # Get the last node of the flattened left subtree
                last_node = flatten_tree(node.right)
                # Connect the last node to the right subtree
                last_node.right = right_subtree
            else:
                # If no left subtree, just flatten the right subtree
                last_node = node
            
            # Flatten the right subtree
            if right_subtree:
                last_node = flatten_tree(right_subtree)
            
            return last_node
        
        flatten_tree(root)
        
        # Approach 2: Iterative Solution using Stack
        # Time Complexity: O(n)
        # Space Complexity: O(n) for the stack
        """
        if not root:
            return
        
        stack = [root]
        prev = None
        
        while stack:
            curr = stack.pop()
            
            if prev:
                prev.right = curr
                prev.left = None
            
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
                
            prev = curr
        """