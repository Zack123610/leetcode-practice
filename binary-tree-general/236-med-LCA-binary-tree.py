# Leetcode 236: Lowest Common Ancestor of a Binary Tree
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor_recursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Recursive approach
        Time Complexity: O(N) where N is the number of nodes
        Space Complexity: O(H) where H is the height of the tree (due to recursion stack)
        """
        # Base cases
        if not root or root == p or root == q:
            return root
        
        # Recursively search in left and right subtrees
        left = self.lowestCommonAncestor_recursive(root.left, p, q)
        right = self.lowestCommonAncestor_recursive(root.right, p, q)
        
        # If both left and right are not None, current root is LCA
        if left and right:
            return root
        
        # Return the non-None value (either left or right)
        return left if left else right

    def lowestCommonAncestor_iterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Iterative approach using parent pointers
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        # Stack for tree traversal
        stack = [root]
        
        # Dictionary for parent pointers
        parent = {root: None}
        
        # Iterate until we find both p and q
        while p not in parent or q not in parent:
            node = stack.pop()
            
            # If left child exists, add it to stack and update parent
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            
            # If right child exists, add it to stack and update parent
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        # Ancestors set for node p
        ancestors = set()
        
        # Process all ancestors for node p using parent pointers
        while p:
            ancestors.add(p)
            p = parent[p]
        
        # The first ancestor of q which appears in p's ancestor set is LCA
        while q not in ancestors:
            q = parent[q]
        
        return q

# Example usage:
if __name__ == "__main__":
    # Create a sample tree
    #       3
    #      / \
    #     5   1
    #    / \  / \
    #   6  2  0  8
    #     / \
    #    7   4
    
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    
    solution = Solution()
    
    # Test case 1: LCA of nodes 5 and 1
    p = root.left  # node 5
    q = root.right  # node 1
    lca = solution.lowestCommonAncestor_recursive(root, p, q)
    print(f"LCA of {p.val} and {q.val} is: {lca.val}")  # Expected output: 3
    
    # Test case 2: LCA of nodes 5 and 4
    p = root.left  # node 5
    q = root.left.right.right  # node 4
    lca = solution.lowestCommonAncestor_iterative(root, p, q)
    print(f"LCA of {p.val} and {q.val} is: {lca.val}")  # Expected output: 5

