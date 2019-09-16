class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j, intersection = 0, 0, set()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                intersection.add(nums1[i])
                i += 1
                j += 1
        return intersection
# O(m+n) time -if inputs aee sorted
# O(1) space excluding intersection result