#!/usr/bin/env python3

#https://leetcode.com/problems/univalued-binary-tree/submissions/

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:    
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.root_val = root.val
        boolean_value = True
        return self.preorder(root)
            
    def preorder(self,root):
        if root:
            if root.val != self.root_val:
                print("yes")
                return False
        return self.preorder(root.left) and self.preorder(root.right)
        
        

#O(n) time and O(H) space

