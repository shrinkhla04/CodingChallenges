#!/usr/bin/env python3
class Solution(object):
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dict_two_sum={}

        for i in range(len(nums)):
            print(i)
            if (target - nums[i]) not in dict_two_sum:
                dict_two_sum[nums[i]] = i
            else:
                return [i,dict_two_sum[target-nums[i]]]

        
r1=Solution()
        
nums = [2, 7, 11, 15]
target = 9

j=r1.twoSum(nums, target)
print(j)