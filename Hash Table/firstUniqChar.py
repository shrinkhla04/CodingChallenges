class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = [i]
            else:
                s_dict[s[i]] += [i]
        min_index = 999999999999999999
        for k in s_dict.values():
            if len(k) == 1:
                min_index = min(min_index,k[0])
        if min_index == 999999999999999999:
            min_index = -1
        
        return min_index
#O(N) time to build the hash table
#O(1) space