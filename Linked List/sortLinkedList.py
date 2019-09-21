# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #merge two sorted linked lists
    def merge(self,left,right):
        dummy_head = ListNode(0)
        current = dummy_head
        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
                current = current.next
            else:
                current.next = right
                right = right.next
                current = current.next
            current.next = left or right
        return dummy_head.next
    def sortList(self, head: ListNode) -> ListNode:
        #find the middle and apply mergesort
        
        if not head or not head.next: 
            return head
        else:
            prev, slow, fast = None, head, head 
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            
            return self.merge(self.sortList(head), self.sortList(slow))
    
                
        
# O(nlogn) time and O(1) space