#https://leetcode.com/problems/intersection-of-two-arrays/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_nums1 = {}
        if len(nums1) < len(nums2):
            dict_nums = nums1
            k = nums2                 #to occupy O(min(len(nums1), len(nums2))) space
        else:
            dict_nums = nums2
            k = nums1
        for i in dict_nums:
            dict_nums1[i] = 1
        
        intersection = []
        for j in k:
            if j in dict_nums1:
                intersection.append(j)
                dict_nums1.pop(j)
        return intersection
#Time : O(m+n)
#Space : O(min(m,n))