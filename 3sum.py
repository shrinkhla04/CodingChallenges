#!/usr/bin/env python3
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        combined_list=[]
        for i in range(len(nums)-2):#triplet can't be formed if i is equal to len(nums)-1 or len(nums)-2
            for k in range(i+1,len(nums)-1):#if k is equal to len(nums)-1 then triplet can't be formed
                for j in range(k+1,len(nums)):    
                    if nums[i]+nums[k]+nums[j]==0:
                        x=0
                        individual_list=[nums[i],nums[k],nums[j]]
                        if len(combined_list)==0:
                            #print("i j k is {} {} {}" .format(i,j,k))
                            #print("individual list is when len of combined list is 0",individual_list)

                            combined_list.append(individual_list)
                            #print("combined list is when len of combined list is 0 ",combined_list)   
                        else:
                            #print("else i j k is {} {} {}" .format(i,j,k))

                            #print(" else x is ",x)
                            #print(" else individual list is when len of combined list is not equal to 0",individual_list)

                          
                        
                            for triplet in combined_list:
                                #print(" else triplet is",triplet)
                                
                                if triplet[0] in individual_list and triplet[1] in individual_list and triplet[2] in individual_list :
                                    #print("x in if is ", x)

                                    x=1

                                    break
                            #print("x is before x==1", x)

                                
                            if x!=1:        
                                combined_list.append(individual_list)
                                print("else combined list is when len of combined list is not equal to 0 ",combined_list)   
                                
        print(combined_list)
   
        return combined_list

r1=Solution()
nums=[0,3,0,1,1,-1,-5,-5,3,-3,-3,0]

r1.threeSum(nums)
