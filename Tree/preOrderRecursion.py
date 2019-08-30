#!/usr/bin/env python3

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.preorder_list = []
    def preorder(self, root: 'Node'):
        if root:
            self.preorder_list.append(root.val)
            for i in root.children:
                self.preorder(i)
        return self.preorder_list

#O(n) time and O(H) space
