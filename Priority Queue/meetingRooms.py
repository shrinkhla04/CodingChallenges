class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x[0])
        #sort the meeting timings according to their start time
        min_heap = []
        heapq.heappush(min_heap, intervals[0][1])
        #push the ending time of first meeting
        """we only need to keep track of the ending timings as if 
        the ending time of a meeting which is going to be finished the earliest
        is lesser than the starting time of the new meeting for which the meeting room is
        to be scheduled then no new meeting room i sto be assigned and we can pop this 
        meeting with the earliest ending time from the heap and add the new meeting's ending time to the heap
        In case the new meeting's ending time is lesser than the meeting with the earliest ending time then the new meeting's ending will
        be pushed to the heap without popping the ending time of the meeting which ends the earliest , in other words
        a new meeting room would be assigned
        """
        for i in intervals[1:]:
            if min_heap[0] <= i[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, i[1])
        return len(min_heap)
     #O(NlogN) time and #O(N) space as in worst case we would have to assign a new meeting room to each of the meeting
