#https://leetcode.com/problems/student-attendance-record-i/
class Solution:
    import re
    def checkRecord(self, s: str) -> bool:
        return not (re.search('.*A.*A.*', s) or re.search('LLL',s))
#O(n) time and O(1) space