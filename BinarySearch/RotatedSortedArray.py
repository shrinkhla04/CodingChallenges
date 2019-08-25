#!/usr/bin/env python3

class Solution(object):
   def search(self, nums, target) -> int:
        def rotation_index_search(low,high):
            if nums[low] < nums[high]:
                return -1
            else:
                while low <= high:
                    mid = (low + high) // 2
                    print(low,high,mid)
                    if nums[mid+1] < nums[mid]:
                        rotation_index = mid + 1
                        return rotation_index
                    elif (nums[mid] < nums[low]):
                        high = mid - 1
                    else:
                        low = mid + 1
                    
        
        def target_search(low,high,target):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                    
            return -1
        
        if len(nums) == 0:
            target_index = -1
        elif len(nums) == 1:
            if nums[0]==target:
                target_index=0
            else:
                target_index=-1
                
        
        else:
            rotation_index=rotation_index_search(0, len(nums) - 1)                
            print("Rotation index is",  rotation_index) 
            if rotation_index == -1:
                target_index = target_search(0, len(nums) - 1, target)

            else:

                if target >= nums[rotation_index] and target <= nums[len(nums) - 1]:
                    target_index=target_search(rotation_index, len(nums) - 1, target)
                    print("Target index is ",target_index)

                else:
                    target_index=target_search(0, rotation_index - 1, target)
                    print("Target index is ",target_index)

           
        
            
        return target_index



                

r1=Solution()
        
nums = [6,7,8,1,2,3,4,5]
target = 6

j=r1.search(nums, target)
print(j)


                
            
            
        