# Leetcode 1086: High Five
# Link: https://leetcode.com/problems/high-five/

from typing import List
import heapq

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        """
        Given a list of items where items[i] = [IDi, scorei], 
        return the average of the top 5 scores for each student.
        
        Time Complexity: O(n log n) where n is the number of items
        Space Complexity: O(n) for storing student scores
        """
        # Dictionary to store scores for each student
        student_scores = {}
        
        # Group scores by student ID
        for student_id, score in items:
            if student_id not in student_scores:
                student_scores[student_id] = []
            student_scores[student_id].append(score)
        
        result = []
        
        # For each student, calculate average of top 5 scores
        for student_id in sorted(student_scores.keys()):
            scores = student_scores[student_id]
            # Sort in descending order and take top 5
            top_5_scores = sorted(scores, reverse=True)[:5]
            average = sum(top_5_scores) // len(top_5_scores)
            result.append([student_id, average])
        
        return result


class SolutionHeap:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        """
        Alternative solution using heaps for better performance when dealing with many scores per student.
        
        Time Complexity: O(n log 5) = O(n) where n is the number of items
        Space Complexity: O(n) for storing student scores
        """
        from collections import defaultdict
        
        student_heap = defaultdict(list)

        for xid, xscore in items:
            heapq.heappush(student_heap[xid], xscore)

            # Keep only top 5 scores
            if len(student_heap[xid]) > 5:
                heapq.heappop(student_heap[xid])
        
        res = []
    
        for xid in sorted(student_heap.keys()):
            # top five scores
            scores = student_heap[xid]
            avg5scores = sum(scores) // len(scores)
            res.append([xid, avg5scores])

        return res



class SolutionCounter:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        """
        Solution using Counter for cases where we need to handle duplicate scores.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        from collections import defaultdict
        
        student_scores = defaultdict(list)
        
        for student_id, score in items:
            student_scores[student_id].append(score)
        
        result = []
        
        for student_id in sorted(student_scores.keys()):
            scores = student_scores[student_id]
            # Sort in descending order and take top 5
            top_5 = sorted(scores, reverse=True)[:5]
            average = sum(top_5) // len(top_5)
            result.append([student_id, average])
        
        return result


# Test cases
def test_solutions():
    solution = Solution()
    solution_heap = SolutionHeap()
    solution_counter = SolutionCounter()
    
    # Test case 1
    items1 = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    expected1 = [[1,87],[2,88]]
    
    result1 = solution.highFive(items1)
    result1_heap = solution_heap.highFive(items1)
    result1_counter = solution_counter.highFive(items1)
    
    print("Test Case 1:")
    print(f"Input: {items1}")
    print(f"Expected: {expected1}")
    print(f"Solution: {result1}")
    print(f"SolutionHeap: {result1_heap}")
    print(f"SolutionCounter: {result1_counter}")
    print(f"All solutions correct: {result1 == expected1 == result1_heap == result1_counter}")
    print()
    
    # Test case 2
    items2 = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
    expected2 = [[1,100],[7,100]]
    
    result2 = solution.highFive(items2)
    result2_heap = solution_heap.highFive(items2)
    result2_counter = solution_counter.highFive(items2)
    
    print("Test Case 2:")
    print(f"Input: {items2}")
    print(f"Expected: {expected2}")
    print(f"Solution: {result2}")
    print(f"SolutionHeap: {result2_heap}")
    print(f"SolutionCounter: {result2_counter}")
    print(f"All solutions correct: {result2 == expected2 == result2_heap == result2_counter}")
    print()
    
    # Test case 3 - Edge case with less than 5 scores
    items3 = [[1,90],[1,80]]
    expected3 = [[1,85]]
    
    result3 = solution.highFive(items3)
    result3_heap = solution_heap.highFive(items3)
    result3_counter = solution_counter.highFive(items3)
    
    print("Test Case 3 (Edge case - less than 5 scores):")
    print(f"Input: {items3}")
    print(f"Expected: {expected3}")
    print(f"Solution: {result3}")
    print(f"SolutionHeap: {result3_heap}")
    print(f"SolutionCounter: {result3_counter}")
    print(f"All solutions correct: {result3 == expected3 == result3_heap == result3_counter}")


if __name__ == "__main__":
    test_solutions()