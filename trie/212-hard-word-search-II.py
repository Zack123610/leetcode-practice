# Leetcode 212: Word Search II
# Link: https://leetcode.com/problems/word-search-ii/

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True


class Solution:
    '''
    Backtracking with Trie
    Time Complexity: O(N * 4 * 3^(L-1))
    Space Complexity: O(N)
    '''

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Create Trie
        root = TrieNode()
        for word in words:
            root.addWord(word)

        # consts
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        res = set()

        # Define DFS
        def dfs(r, c, node, word):
            # Terminating condition
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r, c) in visited:
                return

            if board[r][c] not in node.children:
                return
            
            ch = board[r][c]
            if ch not in node.children:
                return

            visited.add((r, c))
            cur = node.children[ch]
            word += ch

            if cur.endOfWord:
                res.add(word)
                
            # iterate
            dfs(r + 1, c, cur, word)
            dfs(r - 1, c, cur, word)
            dfs(r, c + 1, cur, word)
            dfs(r, c - 1, cur, word)

            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)

            
        