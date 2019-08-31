#!/usr/bin/env python3

#https://leetcode.com/problems/increasing-order-search-tree/
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
#using inorder traversal
class Solution:
    def __init__(self):
        self.dummy_head = TreeNode(0) 
        self.current = self.dummy_head
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root.left:      
            self.increasingBST(root.left)
        
        self.current.right = TreeNode(root.val)
        self.current = self.current.right
        
        if root.right:
            self.increasingBST(root.right)
        
        return self.dummy_head.right


#O(n) time and O(H) space

