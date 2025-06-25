# Leetcode 433: Minimum Genetic Mutation
# Link: https://leetcode.com/problems/minimum-genetic-mutation/

from collections import deque
from typing import List

# My solution: BFS
class mySolution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        n = len(startGene)

        queue = deque([(startGene, 0)])
        options = ['A', 'C', 'G', 'T']
        visited = {startGene}
        bank_set = set(bank)

        while queue:
            curr, moves = queue.popleft()

            if curr == endGene:
                return moves

            for i in range(n):
                for option in options:
                    if option == curr[i]:
                        continue
                    mutated = curr[:i] + option + curr[i+1:]

                    if mutated in bank_set and mutated not in visited:
                        visited.add(mutated)
                        queue.append((mutated, moves + 1))
        
        return -1

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        Find the minimum number of mutations to transform startGene to endGene.
        
        Args:
            startGene: Starting gene sequence (8 characters long, A/C/G/T)
            endGene: Target gene sequence (8 characters long, A/C/G/T)
            bank: List of valid gene sequences
            
        Returns:
            Minimum number of mutations, or -1 if impossible
        """
        # If endGene is not in bank, it's impossible
        if endGene not in bank:
            return -1
        
        # Convert bank to set for O(1) lookup
        bank_set = set(bank)
        
        # BFS queue: (gene, mutations_count)
        queue = deque([(startGene, 0)])
        
        # Track visited genes to avoid cycles
        visited = {startGene}
        
        # Possible mutations (A, C, G, T)
        mutations = ['A', 'C', 'G', 'T']
        
        while queue:
            current_gene, mutations_count = queue.popleft()
            
            # If we reached the target, return the count
            if current_gene == endGene:
                return mutations_count
            
            # Try all possible single-character mutations
            for i in range(8):  # Gene length is always 8
                for mutation in mutations:
                    # Create new gene with one character changed
                    new_gene = current_gene[:i] + mutation + current_gene[i+1:]
                    
                    # Check if it's a valid mutation (in bank and not visited)
                    if new_gene in bank_set and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, mutations_count + 1))
        
        # If we can't reach endGene
        return -1

# Alternative solution using bidirectional BFS for better performance
class SolutionOptimized:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        Optimized solution using bidirectional BFS.
        """
        if endGene not in bank:
            return -1
        
        bank_set = set(bank)
        mutations = ['A', 'C', 'G', 'T']
        
        # Two sets for bidirectional BFS
        start_set = {startGene}
        end_set = {endGene}
        visited = set()
        
        mutations_count = 0
        
        while start_set and end_set:
            # Always work with the smaller set for efficiency
            if len(start_set) > len(end_set):
                start_set, end_set = end_set, start_set
            
            next_level = set()
            
            for gene in start_set:
                if gene in end_set:
                    return mutations_count
                
                if gene in visited:
                    continue
                
                visited.add(gene)
                
                # Try all possible mutations
                for i in range(8):
                    for mutation in mutations:
                        new_gene = gene[:i] + mutation + gene[i+1:]
                        if new_gene in bank_set and new_gene not in visited:
                            next_level.add(new_gene)
            
            start_set = next_level
            mutations_count += 1
        
        return -1

# Test cases
def test_solution():
    solution = Solution()
    
    # Test case 1
    start1 = "AACCGGTT"
    end1 = "AACCGGTA"
    bank1 = ["AACCGGTA"]
    assert solution.minMutation(start1, end1, bank1) == 1
    
    # Test case 2
    start2 = "AACCGGTT"
    end2 = "AAACGGTA"
    bank2 = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    assert solution.minMutation(start2, end2, bank2) == 2
    
    # Test case 3
    start3 = "AAAAACCC"
    end3 = "AACCCCCC"
    bank3 = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    assert solution.minMutation(start3, end3, bank3) == 3
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()