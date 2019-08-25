class Solution:
	def dailyTemperatures(self, T):
		stack, answer = [], [0]*len(T)

		for i in range(len(T)):
			while stack != [] and T[i] > T[stack[-1]]:
				answer[stack[-1]] = i - stack[-1]
				stack.pop()
				
			stack.append(i)		

		return answer



solution_object = Solution()
print(solution_object.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
