#https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        
        for k in range(len(haystack)-len(needle) + 1):
            if haystack[k:len(needle)+k] == needle:
                return k
        return -1
            
 #O(n*m) time as for every k a substring equal to length of m will be compared to the needle
 #O(n*m) space as for every k a substring equal to the length of m will be produced