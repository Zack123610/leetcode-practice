# Leetcode 98: Validate Binary Search Tree
# Link: https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Solution 1: Recursive approach with min/max bounds
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree (due to recursion stack)
        """
        def validate(node, min_val, max_val):
            if not node:
                return True
            
            # Check if current node's value is within valid range
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively check left and right subtrees
            return (validate(node.left, min_val, node.val) and 
                   validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))
    
    def isValidBST_iterative(self, root: Optional[TreeNode]) -> bool:
        """
        Solution 2: Iterative approach using inorder traversal
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree
        """
        if not root:
            return True
            
        stack = []
        curr = root
        prev = None
        
        while stack or curr:
            # Reach the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process current node
            curr = stack.pop()
            
            # Check if current value is greater than previous value
            if prev is not None and curr.val <= prev.val:
                return False
            
            prev = curr
            curr = curr.right
            
        return True
