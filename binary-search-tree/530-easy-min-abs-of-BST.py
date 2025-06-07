# Leetcode 530: Minimum Absolute Difference in BST
# Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # Iterative solution using stack
        def iterative_solution():
            stack = []
            curr = root
            prev = None
            min_diff = float('inf')
            
            while stack or curr:
                # Reach the leftmost node
                while curr:
                    stack.append(curr)
                    curr = curr.left
                
                curr = stack.pop()
                
                if prev is not None:
                    min_diff = min(min_diff, curr.val - prev.val)
                prev = curr
                
                curr = curr.right
            
            return min_diff
        
        # Recursive solution
        def recursive_solution():
            def inorder(node):
                if not node:
                    return
                
                inorder(node.left)
                
                nonlocal prev, min_diff
                if prev is not None:
                    min_diff = min(min_diff, node.val - prev.val)
                prev = node
                
                inorder(node.right)
            
            prev = None
            min_diff = float('inf')
            inorder(root)
            return min_diff
        
        # You can use either solution
        return iterative_solution()
        # return recursive_solution()