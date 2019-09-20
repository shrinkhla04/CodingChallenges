#https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = []
        for i in intervals:    
            if res and i[0] <= res[-1][1]:
                res[-1][1] = max(i[1],res[-1][1])
            else:
                res += i,
            
        return res
#O(nlogn) time for sorting and O(n) time to iterate over the intervals
#Final time complexity : O(nlogn)
#O(n) space for res in worst case when no intervals merge