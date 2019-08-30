#!/usr/bin/env python3

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    range_sum = 0
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root.left and L < root.val:
            self.rangeSumBST(root.left, L, R)
        if root.val >= L and root.val <= R:
            self.range_sum += root.val
        if root.right and R > root.val:
            self.rangeSumBST(root.right, L, R)
        return self.range_sum
            