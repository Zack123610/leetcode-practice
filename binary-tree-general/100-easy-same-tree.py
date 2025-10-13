# Leetcode 100: Same Tree
# Link: https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive solution
    '''
    Time complexity: O(n)
    Space complexity: O(n) n - number of nodes
    '''
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # If both nodes are None, they are the same
        if not p and not q:
            return True
        # If one is None and the other isn't, they're different
        if not p or not q:
            return False
        # Check current values and recursively check left and right subtrees
        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))

    # Iterative solution using BFS
    def isSameTreeIterative(self, p: TreeNode, q: TreeNode) -> bool:
        # Create a queue for BFS
        queue = [(p, q)]
        
        while queue:
            node1, node2 = queue.pop(0)
            
            # If both nodes are None, continue
            if not node1 and not node2:
                continue
            # If one is None and the other isn't, they're different
            if not node1 or not node2:
                return False
            # If values are different, trees are different
            if node1.val != node2.val:
                return False
            
            # Add left and right children to queue
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        
        return True

    # Iterative DFS solution using stack
    def isSameTreeDFS(self, p: TreeNode, q: TreeNode) -> bool:
        # Create a stack for DFS
        stack = [(p, q)]
        
        while stack:
            node1, node2 = stack.pop()
            
            # If both nodes are None, continue
            if not node1 and not node2:
                continue
            # If one is None and the other isn't, they're different
            if not node1 or not node2:
                return False
            # If values are different, trees are different
            if node1.val != node2.val:
                return False
            
            # Add right and left children to stack
            # Note: We add right first so that left is processed first (LIFO)
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
        
        return True

# Example usage:
if __name__ == "__main__":
    # Create two identical trees
    # Tree 1:    1
    #           / \
    #          2   3
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    
    # Tree 2:    1
    #           / \
    #          2   3
    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)
    
    sol = Solution()
    print(sol.isSameTree(tree1, tree2))  # Output: True
    print(sol.isSameTreeIterative(tree1, tree2))  # Output: True
    print(sol.isSameTreeDFS(tree1, tree2))  # Output: True