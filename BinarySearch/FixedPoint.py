#!/usr/bin/env python3
class Solution: 
    def fixedPoint(self, A: List[int]) -> int:
        def binary_search(A, low, high):
            mid=(low+high)//2
            if A[mid]==mid:
                return mid
            elif A[mid]>mid:
                low=low
                high=mid-1
                return binary_search(A,low,high)
            elif A[mid]<mid:
                low=mid+1
                high=high 
                return binary_search(A,low,high)               
            else:
                return -1
        

        return binary_search(A,0,(len(A)-1))

            






list_of_numbers=[-10,-5,0,3,7]
high=len(list_of_numbers)
object_of_solution_class=Solution()
j=object_of_solution_class.fixedPoint(list_of_numbers)
print(j)