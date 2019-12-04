class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1) #dp[i] would indicate if s[:i] can be formed from words in dictionary
        dp[0] = True #dp[0] represents an empty string and we can say that an empty string is part of s
        
        for i in range(1,len(s)+1):
            #the for loop will iterate from 1 to len(s) + 1 to check the possibility of s[:i] being represented by words in dictionary
            for w in wordDict:
                if dp[i-len(w)] and s[i-len(w):i] == w:
                    #if at an index i-len(w) dp[i] is true then this implies that s[:i-len(w)] can be represented by given words in dictionary, so now if we check if s[i-len(w):i] is present in the word dictionary then we can say that s[:i] can be represented by words in the dictionary and hence dp[:i] will be true then 
                    dp[i] = True
        return dp[-1]
    
    #Time complexity : O(K*len(s)) where K is the total content of wordDict
                    