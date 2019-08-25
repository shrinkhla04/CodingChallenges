#!/usr/bin/env python3
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) //2 #mid will be the root
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[(mid+1): ])
        return root

        """This will be a height balanced tree as if there are odd numbers in the list then the left and right subtree will have equal number of digits"""

        """In case of even numbers in the list the left subtree will have one more digit than in the right subtree""""

print(Solution.sortedArrayToBST([-10,-3,0,5,9]))
