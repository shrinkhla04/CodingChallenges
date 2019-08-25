#!/usr/bin/env python3

class Solution:
    def calPoints(self, ops):
    	baseball_game_points=[]
    	for i in ops:
    		if i == "+":
    			baseball_game_points.append(baseball_game_points[-1]+baseball_game_points[-2])
    		elif i  == "D":
    			baseball_game_points.append(2 * baseball_game_points[-1])
    		elif i == "C":
    			baseball_game_points.pop()
    		else:
    			baseball_game_points.append(int(i))

    	return sum(baseball_game_points)

calPoints_object=Solution()
print(calPoints_object.calPoints(["5","2","C","D","+"]))






        