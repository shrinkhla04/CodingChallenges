#!/usr/bin/env python3

class Solution:
    def backspaceCompare(self, S, T):
    	S_stack=[]
    	T_stack=[]



    	for i in S:
    		if i != '#':
    			S_stack.append(i)
    		else:
    			print(i)
    			if len(S_stack) != 0:
    				S_stack.pop()


    	for i in T:
    		if i != '#':
    			T_stack.append(i)
    		else:
    			print(i)
    			if len(T_stack) != 0 :
    				T_stack.pop()



    	"""

    	for i in range(len(S)):
    		print(S[i])

    		if i == (len(S) - 1):
    			if  S[i] !='#' :
    				S_stack.append(S[i])
    		else:

    			if S[i] != '#':
    			    if S[i+1] == '#':
    			    	i=i+1
    			    else:
    			    	S_stack.append(S[i])
    			else:
    				if not S_stack:
    					S_stack.pop()

    		print(S_stack)
    	print("s_tack is",S_stack)


    	for i in range(len(T)):
    		print(T[i])

    		if i == (len(T) - 1):
    			if  T[i] !='#' :
    				T_stack.append(T[i])
    		else:

    			if T[i] != '#':
    			    if T[i+1] == '#':
    			    	continue
    			    else:
    			    	T_stack.append(S[i])
    			else:
    				if len(T_stack)==0:
    					T_stack.pop()

    		print(T_stack)"""

    	#print(T_stack)

    	print(S_stack)
    	print(T_stack)
    		
    	if len(S_stack)==len(T_stack):
    		if len(S_stack)==0:
    			return True
    		else:

    			for k in range(len(S_stack)):
    				if S_stack[k] == T_stack[k]:
    					return True
    				else:
    					return False
    	else:
    		return False


solution_object=Solution()
S="a#c"
T="b"
print(solution_object.backspaceCompare(S,T))





        