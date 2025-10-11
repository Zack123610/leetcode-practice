# Leetcode 20: Valid Parenthesis
# Link: https://leetcode.com/problems/valid-parentheses/

class SolutionLeetcode:
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ')': '(', '}': '{', ']': '['}

        for ch in s:                
            if ch in closeToOpen:
                if stack and stack[-1] == closeToOpen[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return True if not stack else False

class SolutionSelf:
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def isValid(self, s: str) -> bool:

        stack = []

        for idx, ch in enumerate(s):
            if ch in '({[':
                stack.append(ch)
            
            if ch in ')}]' and not stack:
                return False

            if ch in ')}]' and stack:
                cur = stack.pop()
                if ch == ')':
                    if cur != '(':
                        return False
                elif ch == '}':
                    if cur != '{':
                        return False
                else:
                    if cur != "[":
                        return False
        
        return True if not stack else False