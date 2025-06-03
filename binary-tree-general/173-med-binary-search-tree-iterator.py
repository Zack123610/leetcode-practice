# Leetcode 173: Binary Search Tree Iterator
# Link: https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        # Initialize the stack for storing nodes
        self.stack = []
        # Push all left nodes into the stack
        self._push_all_left(root)
    
    def _push_all_left(self, node):
        # Helper function to push all left nodes into the stack
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self) -> int:
        # Get the next smallest number
        node = self.stack.pop()
        # If the node has a right child, push all left nodes of the right subtree
        if node.right:
            self._push_all_left(node.right)
        return node.val
    
    def hasNext(self) -> bool:
        # Check if there are more nodes to traverse
        return len(self.stack) > 0

# Test cases
def test_bst_iterator():
    # Create a sample BST: [7,3,15,null,null,9,20]
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    
    # Initialize the iterator
    iterator = BSTIterator(root)
    
    # Test the iterator
    assert iterator.next() == 3    # Return 3
    assert iterator.next() == 7    # Return 7
    assert iterator.hasNext()      # Return true
    assert iterator.next() == 9    # Return 9
    assert iterator.hasNext()      # Return true
    assert iterator.next() == 15   # Return 15
    assert iterator.hasNext()      # Return true
    assert iterator.next() == 20   # Return 20
    assert not iterator.hasNext()  # Return false
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_bst_iterator()

