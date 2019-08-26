#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def height(self,p):
        if not p.left and not p.right:
            return 0
        elif p.left and p.right:
            return 1 + max(self.height(p.left),self.height(p.right))
        elif p.left and not p.right:
            return 1 + self.height(p.left)
        elif p.right and not p.left:
            return 1+ self.height(p.right)
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        elif not root.left and not root.right:
            return True
        elif root.left and not root.right:
            return self.height(root.left) == 0        
        elif root.right and not root.left:
            return self.height(root.right) == 0  
        elif root.left and root.right:
            return self.isBalanced(root.left) and self.isBalanced(root.right) and (0 <= abs(self.height(root.left) - self.height(root.right)) <= 1)
            
            