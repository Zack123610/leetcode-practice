# Leetcode 105: Construct Binary Tree from Preorder and Inorder Traversal
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Time complexity: O(n^2)
    Space complexity: O(n)
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[ 1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

class SolutionOptimized:
    '''
    Time complexity: O(n)
    Space complexity: O(n)
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        
        inorder_map = {val: i for i, val in enumerate(inorder)}
        preorder_index = 0
        
        def helper(left, right):
            if left > right:
                return
            
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)
            preorder_index += 1
            root.left = helper(left, inorder_map[root_val] - 1)
            root.right = helper(inorder_map[root_val] + 1, right)
            return root
        
        return helper(0, len(inorder) - 1)