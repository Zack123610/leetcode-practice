# Leetcode 199: Binary Tree Right Side View
# Link: https://leetcode.com/problems/binary-tree-right-side-view/

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            qLen = len(queue)

            for i in range(qLen):
                node = queue.popleft()
                
                # If it's the last node in the current level, add to result
                if i == qLen - 1:
                    result.append(node.val)
                
                # Add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
