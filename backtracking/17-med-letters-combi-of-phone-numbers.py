# Leetcode 17: Letter Combinations of a Phone Number
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

class MySolution:
    '''
    Time Complexity: O(4^n * n)
    The total number of recursive function calls will be 4^n
    Copying of the current combination takes (n) time.
    
    Space Complexity: O(n)
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []
        n = len(digits)

        def backtrack(pos, curr):
            if len(curr) == n:
                res.append("".join(curr))
                return
            
            for i in range(pos, len(digits)):
                for letter in hashmap[digits[i]]:
                    curr.append(letter)
                    backtrack(i+1, curr)
                    curr.pop()
        
        backtrack(0, [])
        return res
            
class LeetcodeSolution:
    '''
    Time Complexity: O(4^n * n)
    Space Complexity: O(n)
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0:
            return []

        # Map all the digits to their corresponding letters
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return  # Backtrack

            # Get the letters that the current digit maps to, and loop through them
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations