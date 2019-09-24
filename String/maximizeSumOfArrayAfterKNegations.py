class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        k, i = 0, 0
        while k < K and i < len(A):
            if A[i] < 0:
                A[i] = -A[i]
                k += 1
                i += 1
            elif A[i] == 0:
                k = K
                i = len(A)
            elif A[i] > 0:
                A.sort()
                if (K-k) % 2 != 0:
                    A[0] = -A[0]
                k = K
                i = len(A)
                

        return sum(A)
#O(nlogn) time and O(1) space