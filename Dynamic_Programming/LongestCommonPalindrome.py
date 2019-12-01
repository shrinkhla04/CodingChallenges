class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        dp_array = []
        for i in range(len(s)):
            dp_array.append([0]*(i) +[1] + [0]* (len(s) - 1 - i))
        
        max_length = (0,0)
      
        for length in range(1,len(s)):
            for start in range(len(s)-1):
                if length == 1:
                    if s[start] == s[start + 1]:
                        dp_array[start][start + 1] = 1
                        max_length = (start,start+1)
                    else:
                        dp_array[start][start + 1] = 0
                else:
                    if start + length >= len(s):
                        break
                    else:
                        if s[start] == s[start + length]:
                            if dp_array[start+1][start+length - 1] == 1:
                                dp_array[start][start + length] = 1
                                max_length = (start,start + length)
                        else:
                            dp_array[start][start + length] = 0

        return s[max_length[0]:max_length[1]+1]
#O(n2 ) time and O(n2) space