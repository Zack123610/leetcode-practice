# Leetcode 323: Number of Connected Components in an Undirected Graph
# Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

from typing import List
from collections import defaultdict, deque

class Solution:
    '''
    BFS + Connected Components
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    '''
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Build adjacency list for Undirected Graph
        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        visited = set()
        res = 0

        def bfs(node):
            q = deque([node])
            
            while q:

                curr = q.popleft()
                visited.add(curr)

                for nei in adjList[curr]:
                    if nei not in visited:
                        q.append(nei)

        for node in range(n):
            if node not in visited:
                res += 1
                bfs(node)
            
        return res