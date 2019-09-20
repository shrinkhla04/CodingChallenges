#https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)        

# O(nlogn) time as nlogn time for sorting and O(n) time for sorted list comparison
#O(n) extra space as sorted function will return sorted lists