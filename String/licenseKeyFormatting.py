class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper().replace('-','')[::-1]
        new_S = ""
        return '-'.join(S[i:i+K] for i in range(0,len(S),K))[::-1]
 
#O(n) time and O(n) space