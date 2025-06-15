# Leetcode 133: Clone Graph
# Link: https://leetcode.com/problems/clone-graph/

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Handle empty graph case
        if not node:
            return None
            
        # Solution 1: DFS approach
        def dfs_dfs(node: 'Node', visited: dict) -> 'Node':
            # If node is already visited, return its clone
            if node in visited:
                return visited[node]
            
            # Create a new node
            clone = Node(node.val)
            visited[node] = clone
            
            # Recursively clone all neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs_dfs(neighbor, visited))
            
            return clone
            
        # Solution 2: BFS approach
        def bfs_solution(node: 'Node') -> 'Node':
            if not node:
                return None
                
            # Create a queue for BFS and a dictionary to store visited nodes
            queue = [node]
            visited = {node: Node(node.val)}
            
            while queue:
                current = queue.pop(0)
                
                # Process all neighbors
                for neighbor in current.neighbors:
                    if neighbor not in visited:
                        # Create new node for unvisited neighbor
                        visited[neighbor] = Node(neighbor.val)
                        queue.append(neighbor)
                    
                    # Add the cloned neighbor to the current node's neighbors
                    visited[current].neighbors.append(visited[neighbor])
            
            return visited[node]
        
        # You can use either solution:
        # return dfs_dfs(node, {})  # DFS solution
        return bfs_solution(node)    # BFS solution