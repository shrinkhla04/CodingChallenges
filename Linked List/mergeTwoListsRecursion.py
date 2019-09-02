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
        if l1 and l2:
            if l1.val <= l2.val:
                self.current.next = l1
                self.current = self.current.next
                self.mergeTwoLists(l1.next, l2)
            else:

                self.current.next = l2
                self.current = self.current.next
                self.mergeTwoLists(l1, l2.next)
        elif l1 or l2:

            self.current.next = l1 or l2

        
        return self.merge_list.next
                
#O(m+n) time - as in every recursion call the pointer is increement by one on one of the two lists and will go on until it reaches the end of both the lists 
# O(m+n) space - as the first recursion call does not return until the recursion calls for both the lists are completed so (m+n) memory stack frames will be created
        