class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        nums_dict, degree = {}, 0
        for index, number in enumerate(nums):
            if number not in nums_dict:
                nums_dict[number] = [1, index, index]
            else:
                nums_dict[number][0] += 1
                nums_dict[number][2] = index
            if nums_dict[number][0] > degree:
                degree = nums_dict[number][0]
        length = len(nums)
        for k in nums_dict.values():
            if k[0] == degree:
                length = min(length, k[2] - k[1] + 1)
        return length

#O(N) time and O(1) space