# Leetcode 207: Course Schedule
# Link: https://leetcode.com/problems/course-schedule/

# --- BFS Solution (Kahn's Algorithm) ---
from collections import deque, defaultdict

class SolutionBFS:
    '''
    BFS + Topological Sort
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    '''
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited = 0

        while queue:
            node = queue.popleft()
            visited += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return visited == numCourses

# --- DFS Solution (Cycle Detection) ---
class SolutionDFS:
    '''
    DFS + Cycle Detection
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    '''
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            graph[src].append(dest)

        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

        def dfs(node):
            if visited[node] == 1:
                return False  # cycle detected
            if visited[node] == 2:
                return True   # already checked, no cycle

            visited[node] = 1  # mark as visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2  # mark as visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

