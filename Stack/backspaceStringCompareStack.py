#https://leetcode.com/problems/backspace-string-compare/
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def string_stack(s):
            stack = []
            for i in s:
                if i != '#':
                    stack.append(i)
                elif stack:
                    stack.pop()
                    
            return stack
        return string_stack(S) == string_stack(T)
#o(M+N) time and O(M+N) space
                    
                    
        