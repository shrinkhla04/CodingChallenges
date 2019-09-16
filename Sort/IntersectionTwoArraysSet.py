#https://leetcode.com/problems/intersection-of-two-arrays/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return set1 & set2
#O(m+n) time average and 0(m*n) worst case when load factor is high
#0(m+n) space for worst case when all elements are different