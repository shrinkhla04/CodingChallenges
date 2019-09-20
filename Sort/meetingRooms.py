
#https://leetcode.com/problems/meeting-rooms/
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x : x[0]) #sorting on the basis of start time
        return not any(intervals[i][0] < intervals[i-1][1] for i in range(1,len(intervals))) 

        # comparing if the start time of next meeting is before than the end time of previous meeting
# O(nlogn) time for sorting and O(n) time for iterating over the sorted list of meeting intervals
# Final time complexity : O(nlogn)
#O(1) space
