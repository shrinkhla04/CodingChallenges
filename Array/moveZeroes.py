#https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #we maintain two pointers , one where the non zero element was there before all the zeros in the list(lastNonZeroFound) and other at the non-zero element after the zeros(nextNonZeroFound) in the list

        lastNonZeroFound = -1 
        nextNonZeroFound = 0
        for  nextNonZeroFound in range(len(nums)): #if nextNonZeroFound reaches the end of the list then there are no more non-zero elements in the list which can be use to replace zeros
            if nums[nextNonZeroFound] != 0:
                lastNonZeroFound  += 1  #if nums[nextNonZeroFound] is non-zero then we will swap the 0 at index lastNonZeroFound+1 with nums[nextNonZeroFound]
                nums[nextNonZeroFound], nums[lastNonZeroFound] = nums[lastNonZeroFound], nums[nextNonZeroFound]
                
#O(n) time and O(1) space

