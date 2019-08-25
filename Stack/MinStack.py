#!/usr/bin/env python3

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.

        """
        self._data=[]

    def top(self):
    	if len(self._data) != 0:
    		return self._data[-1][0]
    	else:
    		raise Empty('Stack is empty')

    def pop(self):
    	if len(self._data) != 0:
    		return self._data.pop()
    	else:
    		raise Empty('Stack is empty')        

    def push(self,x):
    	if len(self._data) == 0:
    		self._data.append((x,x))
    	else:
    		self._data.append((x,min(x,self._data[-1][1])))
    
    def getMin(self):
    	if len(self._data) != 0:
    		return self._data[-1][1]
    	else:
    		raise Empty('Stack is empty')

    


        
 

# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
#print(minStack.string_stack)
minStack.push(0)
#print(minStack.string_stack)

minStack.push(-3)
#print(minStack.string_stack)

print(minStack.getMin())
print(minStack.pop())
print(minStack.top())   

print(minStack.getMin())