#!/usr/bin/env python3

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q and p.val != q.val:
            return False
        elif (p and not q) or (q and not p):
            return False
        elif not p and not q:
            return True   
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            
    SolutionObject = Solution()
