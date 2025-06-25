# Leetcode 909: Snakes and Ladders
# Link: https://leetcode.com/problems/snakes-and-ladders/

from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        Find the minimum number of moves to reach the end of the board.
        
        Args:
            board: 2D grid representing the snakes and ladders board
            
        Returns:
            Minimum number of moves, or -1 if impossible

        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        n = len(board)
        
        # Convert 2D coordinates to 1D position and vice versa
        def get_coordinates(pos):
            """Convert 1D position to 2D coordinates (row, col)"""
            r = (pos - 1) // n
            c = (pos - 1) % n
            actual_r = (n - 1) - r # Active order on board is in reverse
            if r % 2 == 1:  # ← FIXED: check parity of logical row from bottom instead of using actual_r
                c = (n - 1) - c
            return actual_r, c

        
        # BFS to find shortest path
        queue = deque([(1, 0)])  # (position, moves)
        visited = {1}
        
        while queue:
            pos, moves = queue.popleft()
            
            # Check if we reached the end
            if pos == n * n:
                return moves
            
            # Try all possible dice rolls (1-6)
            for dice in range(1, 7):
                next_pos = pos + dice
                
                # Check if next position is valid
                if next_pos > n * n:
                    break
                
                # Get coordinates for the next position
                row, col = get_coordinates(next_pos)
                
                # Check if there's a snake or ladder at this position
                if board[row][col] != -1:
                    next_pos = board[row][col]
                
                # If we haven't visited this position yet
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))
        
        return -1  # Impossible to reach the end

# Dijkstra's algorithm solution
import heapq

class Solution3:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        Solution using Dijkstra's algorithm.
        
        This approach treats the board as a weighted graph where:
        - Each position is a node
        - Each dice roll creates an edge with weight 1
        - Snakes and ladders create edges with weight 0 (instant teleport)
        
        Time Complexity: O(n^2 * log(n^2)) due to heap operations
        Space Complexity: O(n^2)
        """
        n = len(board)
        
        def get_coordinates(pos):
            """Convert 1D position to 2D coordinates (row, col)"""
            r = (pos - 1) // n
            c = (pos - 1) % n
            actual_r = (n - 1) - r  # Active order on board is in reverse
            if r % 2 == 1:  # Check parity of logical row from bottom
                c = (n - 1) - c
            return actual_r, c
        
        # Priority queue: (distance, position)
        pq = [(0, 1)]
        # Distance from start to each position
        distances = {1: 0}
        # Target position
        target = n * n
        
        while pq:
            current_dist, current_pos = heapq.heappop(pq)
            
            # If we've already found a shorter path, skip
            if current_dist > distances.get(current_pos, float('inf')):
                continue
            
            # If we reached the target, return the distance
            if current_pos == target:
                return current_dist
            
            # Try all possible dice rolls
            for dice in range(1, 7):
                next_pos = current_pos + dice
                
                # Check if next position is valid
                if next_pos > target:
                    break
                
                # Get coordinates for the next position
                row, col = get_coordinates(next_pos)
                
                # Check if there's a snake or ladder
                if board[row][col] != -1:
                    next_pos = board[row][col]
                
                # Calculate new distance (always +1 for a move)
                new_dist = current_dist + 1
                
                # If this path is shorter than previously found
                if new_dist < distances.get(next_pos, float('inf')):
                    distances[next_pos] = new_dist
                    heapq.heappush(pq, (new_dist, next_pos))
        
        return -1  # Impossible to reach the target

# Alternative Dijkstra's solution with adjacency list approach
class Solution4:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        Alternative Dijkstra's solution using adjacency list representation.
        
        This version explicitly builds the graph first, then applies Dijkstra's.
        """
        n = len(board)
        
        def get_coordinates(pos):
            """Convert 1D position to 2D coordinates (row, col)"""
            r = (pos - 1) // n
            c = (pos - 1) % n
            actual_r = (n - 1) - r
            if r % 2 == 1:
                c = (n - 1) - c
            return actual_r, c
        
        def build_graph():
            """Build adjacency list representation of the board"""
            graph = {}
            target = n * n
            
            for pos in range(1, target + 1):
                graph[pos] = []
                
                # Add edges for all possible dice rolls
                for dice in range(1, 7):
                    next_pos = pos + dice
                    
                    if next_pos > target:
                        break
                    
                    # Check for snake or ladder
                    row, col = get_coordinates(next_pos)
                    if board[row][col] != -1:
                        next_pos = board[row][col]
                    
                    # Add edge with weight 1
                    graph[pos].append((next_pos, 1))
            
            return graph
        
        def dijkstra(graph, start, target):
            """Dijkstra's algorithm to find shortest path"""
            distances = {node: float('inf') for node in graph}
            distances[start] = 0
            
            pq = [(0, start)]
            
            while pq:
                current_dist, current_node = heapq.heappop(pq)
                
                if current_dist > distances[current_node]:
                    continue
                
                if current_node == target:
                    return current_dist
                
                for neighbor, weight in graph[current_node]:
                    new_dist = current_dist + weight
                    
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))
            
            return -1
        
        graph = build_graph()
        return dijkstra(graph, 1, n * n)

# Test cases
def test_snakes_and_ladders():
    # Test all solutions
    solutions = [Solution(), Solution3(), Solution4()]
    solution_names = ["BFS Solution", "Dijkstra Solution3", "Dijkstra Solution4"]
    
    # Test case 1
    board1 = [
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,35,-1,-1,13,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,15,-1,-1,-1,-1]
    ]
    
    print("Test Case 1:")
    for i, (solution, name) in enumerate(zip(solutions, solution_names)):
        result = solution.snakesAndLadders(board1)
        print(f"  {name}: {result} (Expected: 4)")
    
    # Test case 2
    board2 = [
        [-1,-1],
        [-1,3]
    ]
    
    print("\nTest Case 2:")
    for i, (solution, name) in enumerate(zip(solutions, solution_names)):
        result = solution.snakesAndLadders(board2)
        print(f"  {name}: {result} (Expected: 1)")
    
    # Test case 3
    board3 = [
        [-1,-1,-1],
        [-1,9,8],
        [-1,8,9]
    ]
    
    print("\nTest Case 3:")
    for i, (solution, name) in enumerate(zip(solutions, solution_names)):
        result = solution.snakesAndLadders(board3)
        print(f"  {name}: {result} (Expected: 1)")
    
    # Test case 4 - Impossible case
    board4 = [
        [-1,-1,-1],
        [-1,-1,-1],
        [-1,-1,-1]
    ]
    
    print("\nTest Case 4 (Impossible):")
    for i, (solution, name) in enumerate(zip(solutions, solution_names)):
        result = solution.snakesAndLadders(board4)
        print(f"  {name}: {result} (Expected: 2)")

if __name__ == "__main__":
    test_snakes_and_ladders()