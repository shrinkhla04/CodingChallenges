class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[len(s) -1 - i]
            s[len(s) -1 - i] = temp
#O(n/2) time and O(1) space