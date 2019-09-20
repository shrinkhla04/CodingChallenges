#https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        for i in s:
            if i not in dict_s:
                dict_s[i] = 1
            else:
                dict_s[i] += 1
        for i in t:
            if i not in dict_s:
                return False
            else:
                dict_s[i] -= 1                
                if dict_s[i] < 0:
                    return False
        return True
            
# O(n) time for iterating over s and t 
#O(n) space for hash table
#hash table will take care of unicode characters in anagram as well