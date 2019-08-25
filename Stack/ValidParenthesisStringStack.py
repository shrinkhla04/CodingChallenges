class Solution:
	def isValid(self,s):
		stack=[]
		opening_bracket = '({['
		closing_bracket = ')}]'

		if len(s) == 0: 
		    return True

		for i in s:
		    if i in opening_bracket:
		        stack.append(i)
		    else:
		        if not stack: 
		            return False
		        elif opening_bracket.index(stack[-1]) == closing_bracket.index(i):
		            stack.pop()
		        else:
		            return False
		if not stack:
		    return True
		else : 
		    return False
solution_object = Solution()
print(solution_object.isValid("()("))

