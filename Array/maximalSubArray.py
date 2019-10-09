#https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -2147483648
        local_maximum = global_maximum = nums[0]
        for i in range(1, len(nums)):
            local_maximum = max(nums[i], nums[i] + local_maximum )
            global_maximum = max(local_maximum, global_maximum)
        return global_maximum
#O(n) time and O(1) space