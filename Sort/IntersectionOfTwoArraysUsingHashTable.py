#https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_nums1 = {}
        for i in nums1:
            if i not in dict_nums1:
                dict_nums1[i] = 1
            else:
                dict_nums1[i] += 1
        intersection = []
        for i in nums2:
            if i in dict_nums1:
                intersection.append(i)
                dict_nums1[i] -= 1
                if dict_nums1[i] == 0:
                    dict_nums1.pop(i)
        return intersection
#o(m+n) time and O(m) space