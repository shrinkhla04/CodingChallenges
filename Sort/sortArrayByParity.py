class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ans = [None]*len(A)
        e, o = 0, 1
        for i in A:
            if i % 2 == 0:
                ans[e] = i
                e += 2
            else:
                ans[o] = i
                o +=2 
        return ans
    
#O(n) time and O(n) space for ans