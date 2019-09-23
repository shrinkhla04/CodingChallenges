class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        judge = [0]*N 
        for i in range(len(trust)):
            judge[trust[i][0] - 1] -= 1
            judge[trust[i][1] - 1] += 1
        if (N-1) in judge:
            return 1 + judge.index(N-1)
        else:
            return -1
#O(n) time and O(n) space