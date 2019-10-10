class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry, i, j = 0, len(num1) - 1, len(num2) - 1
        sum_str = ""
        while i > -1 or j > -1:
            n1 = (ord(num1[i]) - ord("0")) if i > -1 else 0
            n2 = (ord(num2[j]) - ord("0")) if j > -1 else 0
            sum_curr =  n1 + n2 + carry
            remainder = sum_curr % 10
            sum_str = str(remainder) + sum_str
            carry = sum_curr // 10
            i -= 1
            j -= 1
        if carry > 0:
            sum_str = str(carry) + sum_str
            
        return sum_str
            
            
            
#O(m+n) time and O(m+n) space