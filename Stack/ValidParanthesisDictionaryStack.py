#!/usr/bin/env python3
class Solution:
	def isValid(self,s):
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


		return stack == [] 
		
		"""in case the all the opening brackets are not closed then this will return false 
		and in case the stack is empty then that implies all the opening brackets were matched in the 
		correct order with the closing brackets"""

solution_object = Solution()
print(solution_object.isValid("()("))

