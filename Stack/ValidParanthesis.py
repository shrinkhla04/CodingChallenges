
https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dictionary ={')':'(','}':'{',']':'['}
        """opening brackets are stored as values so that they can be retrieved for comparison 
        with the last element of the stack"""
        for i in s:
            if i in dictionary.values(): 
                stack.append(i)
            else:
                if not stack or stack.pop() != dictionary[i]: 
                    return False
                """in case the string starts with a closing bracket then return false or if the last 
                element of the stack does not correspond to the closing bracket of i"""


        return not stack

        """in case all the opening brackets are not closed then this will return false 
        and in case the stack is empty then that implies all the opening brackets were matched in the 
        correct order with the closing brackets"""


# O(n) time and O(n) space