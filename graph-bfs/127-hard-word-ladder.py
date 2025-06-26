# Leetcode 127: Word Ladder
# Link: https://leetcode.com/problems/word-ladder/

"""
Problem Description:
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter
- Every si for 1 <= i <= k is in wordList
- Note that beginWord does not need to be in wordList
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.
"""

from collections import deque, defaultdict
from typing import List, Set

class Solution:
    """
    Solution 1: Standard BFS Approach
    Time Complexity: O(N * L * 26) where N is the number of words and L is the length of each word
    Space Complexity: O(N) for the queue and visited set
    """
    def ladderLength_bfs(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Convert wordList to set for O(1) lookup
        wordSet = set(wordList)
        
        # If endWord is not in wordList, no transformation is possible
        if endWord not in wordSet:
            return 0
        
        # BFS queue: (word, level)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            current_word, level = queue.popleft()
            
            # If we reach the endWord, return the level
            if current_word == endWord:
                return level
            
            # Try changing each character in the current word
            for i in range(len(current_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    # Create new word by changing one character
                    new_word = current_word[:i] + char + current_word[i+1:]
                    
                    # If new word is in wordList and not visited
                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, level + 1))
        
        return 0
    
    """
    Solution 2: Bidirectional BFS (Optimized)
    Time Complexity: O(N * L * 26) but with better average case performance
    Space Complexity: O(N)
    """
    def ladderLength_bidirectional_bfs(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return 0
        
        # Two sets for bidirectional BFS
        beginSet = {beginWord}
        endSet = {endWord}
        visited = set()
        level = 1
        
        while beginSet and endSet:
            # Always work with the smaller set for better performance
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            
            nextSet = set()
            
            for word in beginSet:
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + char + word[i+1:]
                        
                        # If we find a word that's in the other set, we've found the path
                        if new_word in endSet:
                            return level + 1
                        
                        if new_word in wordSet and new_word not in visited:
                            visited.add(new_word)
                            nextSet.add(new_word)
            
            beginSet = nextSet
            level += 1
        
        return 0
    
    """
    Solution 3: BFS with Preprocessing (Most Efficient)
    Time Complexity: O(N * L^2) for preprocessing + O(N * L) for BFS
    Space Complexity: O(N * L^2)
    """
    def ladderLength_preprocessing(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Preprocess: create adjacency list using wildcard patterns
        # e.g., "hit" -> "*it", "h*t", "hi*"
        adj = defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)
        
        # BFS
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            word, level = queue.popleft()
            
            if word == endWord:
                return level
            
            # Generate all patterns for current word
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                
                # Check all words that match this pattern
                for neighbor in adj[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
        
        return 0
    
    """
    Solution 4: BFS with Early Termination
    Time Complexity: O(N * L * 26)
    Space Complexity: O(N)
    """
    def ladderLength_early_termination(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            current_word, level = queue.popleft()
            
            # Early termination: if current word is endWord
            if current_word == endWord:
                return level
            
            # Try all possible one-character changes
            for i in range(len(current_word)):
                original_char = current_word[i]
                
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if char == original_char:
                        continue
                    
                    new_word = current_word[:i] + char + current_word[i+1:]
                    
                    if new_word in wordSet and new_word not in visited:
                        # Early termination: if new word is endWord
                        if new_word == endWord:
                            return level + 1
                        
                        visited.add(new_word)
                        queue.append((new_word, level + 1))
        
        return 0

# Test cases
def test_solutions():
    solution = Solution()
    
    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    
    print("Test Case 1:")
    print(f"beginWord: {beginWord1}, endWord: {endWord1}")
    print(f"wordList: {wordList1}")
    print(f"BFS Result: {solution.ladderLength_bfs(beginWord1, endWord1, wordList1)}")
    print(f"Bidirectional BFS Result: {solution.ladderLength_bidirectional_bfs(beginWord1, endWord1, wordList1)}")
    print(f"Preprocessing Result: {solution.ladderLength_preprocessing(beginWord1, endWord1, wordList1)}")
    print(f"Early Termination Result: {solution.ladderLength_early_termination(beginWord1, endWord1, wordList1)}")
    print()
    
    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    
    print("Test Case 2 (No path):")
    print(f"beginWord: {beginWord2}, endWord: {endWord2}")
    print(f"wordList: {wordList2}")
    print(f"BFS Result: {solution.ladderLength_bfs(beginWord2, endWord2, wordList2)}")
    print(f"Bidirectional BFS Result: {solution.ladderLength_bidirectional_bfs(beginWord2, endWord2, wordList2)}")
    print(f"Preprocessing Result: {solution.ladderLength_preprocessing(beginWord2, endWord2, wordList2)}")
    print(f"Early Termination Result: {solution.ladderLength_early_termination(beginWord2, endWord2, wordList2)}")
    print()
    
    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a", "b", "c"]
    
    print("Test Case 3:")
    print(f"beginWord: {beginWord3}, endWord: {endWord3}")
    print(f"wordList: {wordList3}")
    print(f"BFS Result: {solution.ladderLength_bfs(beginWord3, endWord3, wordList3)}")
    print(f"Bidirectional BFS Result: {solution.ladderLength_bidirectional_bfs(beginWord3, endWord3, wordList3)}")
    print(f"Preprocessing Result: {solution.ladderLength_preprocessing(beginWord3, endWord3, wordList3)}")
    print(f"Early Termination Result: {solution.ladderLength_early_termination(beginWord3, endWord3, wordList3)}")

if __name__ == "__main__":
    test_solutions()

