#!/usr/bin/env python3

#https://leetcode.com/problems/leaf-similar-trees/    
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.leafSequence1,self.leafSequence2  = [], []
        
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def preorder_root1(root1):
            if root1:
                if not root1.left and not root1.right:
                    self.leafSequence1.append(root1.val)
                preorder_root1(root1.left)
                preorder_root1(root1.right)
            return self.leafSequence1
                
        def preorder_root2(root2):
            if root2:
                if not root2.left and not root2.right:
                    self.leafSequence2.append(root2.val)
                preorder_root2(root2.left)
                preorder_root2(root2.right)
            return self.leafSequence2
        
#O(m+n) time and O(H1+H2) space
