# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    def __init__(self):
        self.merge_list = ListNode(0)
        self.current = self.merge_list
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        while l1 and l2:
            if l1.val <= l2.val:
                self.current.next = l1
                self.current = self.current.next
                l1 = l1.next
            elif l2.val <= l1.val:

                self.current.next = l2
                self.current = self.current.next
                l2 = l2.next
  
        self.current.next = l1 or l2
        
        
        return self.merge_list.next
#O(m+n) time - as it iterates once over each of the elements of l1 and 
# O(1) space - as only few extra pointers are used 
        