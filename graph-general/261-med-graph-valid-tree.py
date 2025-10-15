# Leetcode 261: Graph Valid Tree
# Link: https://leetcode.com/problems/graph-valid-tree/

from collections import defaultdict, deque
from typing import List

class Solution:
    '''
    BFS + Cycle Detection
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    '''
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Quick necessary condition for a tree
        if len(edges) != n - 1:
            return False

        # Build undirected adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # BFS from node 0 and detect cycles via visited set
        visited = set()
        q = deque([0])

        while q:
            node = q.popleft()

            if node in visited: # If we ever re-visit a node, there's a cycle
                return False

            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    q.append(nei)

        # All nodes must be reachable
        return len(visited) == n
