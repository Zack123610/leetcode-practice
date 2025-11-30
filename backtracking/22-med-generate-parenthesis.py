# Leetcode 22: Generate Parentheses
# Link: https://leetcode.com/problems/generate-parentheses/

from typing import List

class Solution:
    '''
    Backtracking Solution
    Time complexity: O( 4^n / n^(1/2) )
    Space complexity: O( n )
    The space complexity of a recursive call depends on the maximum depth of the recursive call stack, which is 2n
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []

        def backtrack(left, right):
            if len(stack) == 2 * n:
                res.append("".join(stack))
                return
            
            if left < n:
                stack.append("(")
                backtrack(left + 1, right)
                stack.pop()
            
            if right < left:
                stack.append(")")
                backtrack(left, right + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res


class BruteForceSolution:
    from collections import deque
    '''
    Time Complexity: O(2^2n * n)
    Space Complexity: O(2^2n * n)
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(p_string):
            left_count = 0
            for p in p_string:
                if p == "(":
                    left_count += 1
                else:
                    left_count -= 1

                if left_count < 0:
                    return False

            return left_count == 0

        answer = []
        queue = collections.deque([""])
        while queue:
            cur_string = queue.popleft()

            # If the length of cur_string is 2 * n, add it to `answer` if
            # it is valid.
            if len(cur_string) == 2 * n:
                if isValid(cur_string):
                    answer.append(cur_string)
                continue
            queue.append(cur_string + "(")
            queue.append(cur_string + ")")
            
        return answer