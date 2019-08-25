#!/usr/bin/env python3

class Solution:
    def removeDuplicates(self, S):
    	class ArrayStack():
            def __init__(self):
                self._data = [ ]
                
            def __len__(self): 
                return len(self._data)
            
            def is_empty(self):
                return len(self._data) == 0
            
            def push(self, e):
                self._data.append(e)
              
            def pop(self):
                if self.is_empty():                
                    raise Empty( 'Stack is empty' )
                return self._data.pop( )

            def top(self):
            	"""Return (but do not remove) the element at the top of the stack , return raise Empty exception if the stack is empty"""
            	if self.is_empty():

            		raise Empty( 'Stack is empty' ) 
            	return self._data[-1]

            def final_stack(self):

            	return ''.join(self._data)




    	string_stack = ArrayStack()
    	for i in S:
    		if string_stack.is_empty():
    			string_stack.push(i)
    		else:
    			if string_stack.top() == i:
    				string_stack.pop()
    			else:
    				string_stack.push(i)



    	return string_stack.final_stack()





            

r1=Solution()
        
S = "abbaca"


j=r1.removeDuplicates(S)
print(j)
