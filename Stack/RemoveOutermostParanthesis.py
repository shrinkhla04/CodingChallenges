#!/usr/bin/env python3

class Solution:
    def removeOuterParentheses(self, S):
        
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
                
                
                    raise Empty( Stack is empty )
                return self._data.pop( )
            
        primitive_decomposition = ""
        primitive_string = ""
        string_stack = ArrayStack()
        if len(S) > 0:
            for i in S: 
                print(i)
                if i=='(':
                    string_stack.push(i)
                else:
                    string_stack.pop()
                
                primitive_string = primitive_string + i
                print(len(string_stack))
                print(len(primitive_string))

                if string_stack.is_empty(): #if len(primitive_string) is 2 then after removing outer parenthesis an empty primitive string will be added to the primitive decomposition so this step will be redundant then
                    if len(primitive_string) > 2 :
                        
                        print("primitive string with outer",primitive_string)
                        primitive_string=primitive_string[1 : (len(primitive_string) - 1)]
                        print("primitive string without outer", primitive_string)
                        print("primitive decomposition initially",primitive_decomposition)
                        primitive_decomposition = primitive_decomposition + primitive_string
                        print("primitive decomposition afterwards",primitive_decomposition)
                        primitive_string=""
                    if len(primitive_string) == 2 :
                        primitive_string= ""
                        

        return primitive_decomposition




r1=Solution()
        
S = "(()())(())"


j=r1.removeOuterParentheses(S)
print(j)




                    