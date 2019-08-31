#!/usr/bin/env python3

#https://leetcode.com/problems/maximum-depth-of-n-ary-tree/class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
#using inorder traversal
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root:
            if not root.children:
                return 1
            else:
                return 1 + max(self.maxDepth(i) for i in root.children)
        return 0
#O(n) time and O(H) space