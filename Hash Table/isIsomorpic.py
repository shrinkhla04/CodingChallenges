class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_table = {}
        mapped_values = []
        for i in range(len(s)):
            if s[i] not in hash_table:
                if t[i] not in mapped_values :
                    hash_table[s[i]] = t[i]
                    mapped_values.append(t[i])
                else:
                    return False
                    
            else:
                if hash_table[s[i]] != t[i]:
                    return False
        return True
        
                    
# O(n) time and O(n) space