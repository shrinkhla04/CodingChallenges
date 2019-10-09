
#https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """        
        nums2_pointer = n - 1
        nums1_pointer = m - 1
        while nums2_pointer > - 1 and nums1_pointer > -1:
            
            if nums2[nums2_pointer] >= nums1[nums1_pointer]:
                nums1[nums2_pointer + nums1_pointer + 1] = nums2[nums2_pointer]
                nums2_pointer -= 1

            else:
                nums1[nums2_pointer + nums1_pointer + 1] = nums1[nums1_pointer]
                nums1_pointer -= 1
            
        while nums2_pointer > - 1:
            nums1[nums2_pointer + nums1_pointer + 1] = nums2[nums2_pointer]
            nums2_pointer -= 1
#O(n+m) time and O(1) space