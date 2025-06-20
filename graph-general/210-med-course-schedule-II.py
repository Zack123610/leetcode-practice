# Leetcode 210: Course Schedule II
# Link: https://leetcode.com/problems/course-schedule-ii/

# --- BFS Solution (Kahn's Algorithm) ---
from collections import deque, defaultdict

class SolutionBFS:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []

# --- DFS Solution ---
from collections import defaultdict

class SolutionDFS:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)

        visited = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited
        order = []
        self.cycle = False

        def dfs(node):
            if visited[node] == 1:
                self.cycle = True
                return
            if visited[node] == 2:
                return
            
            visited[node] = 1
            for neighbor in graph[node]:
                dfs(neighbor)
            visited[node] = 2
            order.append(node)

        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)
            if self.cycle:
                return []

        return order[::-1]

