# https://leetcode.com/problems/unique-email-addresses/
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email = set()
        for i in emails:
            localDomain = i.split('@')
            localSplitPlus = localDomain[0].split('+')            
            unique_email.add(localSplitPlus[0].replace('.','') + '@' + localDomain[1])
               
            

            
        return len(unique_email)
        #Time Complexity: O(C), C is the total content of emails
        