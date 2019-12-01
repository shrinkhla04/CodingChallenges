class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """sort the array and then look for pairs which when added to the target equal to zero"""
        
        nums.sort()
        answer = []
        for i in range(len(nums)-2):
            if nums[i] > 0: # if nums[i] > 0 then the sum of triplet will be > 0 as sum of three positive numbers is always > 0
                break
            if i > 0  and nums[i] == nums[i-1]: # if nums[i] is same as the previous number then we have already fount a solution for it's target
                continue

            target = 0 - nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r  -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    answer.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1 # we have to increase l and r until we find different values than the previous ones in order to avoid repeated solutions 
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                        
        return answer
#O(n2) time and O(1) space