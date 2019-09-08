#https://leetcode.com/problems/student-attendance-record-i/
class Solution:
    def checkRecord(self, s: str) -> bool:
        count_A = 0
        for i in range(len(s)):
            if s[i] == 'A':
                count_A +=1
                if count_A ==2:
                    return False
            elif i <= len(s) -3 :
                print(i)
                if s[i] == s[i+1] == s[i+2] =='L':
                    return False
        return True
            
#O(n) time and O(1) space