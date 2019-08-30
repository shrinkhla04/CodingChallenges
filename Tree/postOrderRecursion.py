#!/usr/bin/env python3

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.post_order_list = []
    def postorder(self, root: 'Node') -> List[int]:
        if root:         
            for i in root.children:
                self.postorder(i)
            self.post_order_list.append(root.val)
        return self.post_order_list

#O(n) time and O(H) space
