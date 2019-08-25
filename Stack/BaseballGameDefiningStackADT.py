#!/usr/bin/env python3

class Solution:
    def calPoints(self, ops):
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

            def second_top(self):

                """Return (but do not remove) the element at the top of the stack , return raise Empty exception if the stack is empty"""
                if self.is_empty():

                    raise Empty( 'Stack is empty' ) 
                return self._data[-2]

            def sum(self):

                """Return (but do not remove) the element at the top of the stack , return raise Empty exception if the stack is empty"""
                if self.is_empty():

                    raise Empty( 'Stack is empty' ) 
                return sum(self._data)


        string_stack = ArrayStack()
        for i in ops:
            print(i)
            if i == "+":
                string_stack.push(string_stack.top()+string_stack.second_top())
            elif i  == "D":
                string_stack.push(2 * string_stack.top())
            elif i == "C":
                string_stack.pop()
            else:
                string_stack.push(int(i))
            print("sum is ",string_stack.sum())


        return string_stack.sum()

calPoints_object=Solution()
print(calPoints_object.calPoints(["5","2","C","D","+"]))



