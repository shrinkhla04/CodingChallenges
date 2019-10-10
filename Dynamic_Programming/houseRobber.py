class Solution:
    def rob(self, nums: List[int]) -> int:
        max_2_before = 0
        max_1_before = 0
        curr_max = 0
        for i in nums:
            curr_max = max(i+max_2_before, max_1_before)
            max_2_before = max_1_before
            max_1_before = curr_max
        return curr_max

#O(N) time and O(1) space