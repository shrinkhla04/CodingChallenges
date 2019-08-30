#!/usr/bin/env python3

#https://leetcode.com/problems/n-ary-tree-preorder-traversal/

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        preorder_list = []
        if root:
            stack = [root]
            while stack:
                current = stack.pop()
                preorder_list.append(current.val)
                stack.extend(reversed(current.children))
        return preorder_list

#O(n) time and O(n) space
