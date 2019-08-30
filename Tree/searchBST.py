#!/usr/bin/env python3

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root.left and root.val > val:
            return self.searchBST(root.left, val)
        if root.val == val:
            return root
        if root.right and root.val < val:
            return self.searchBST(root.right, val)
            
#O(H) space and O(H) time