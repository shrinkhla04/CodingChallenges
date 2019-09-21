# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        while head and head.next:
            if head.val > head.next.val:
                nodeToInsert = head.next
                nodePreToInsert = dummy_head
                while nodePreToInsert.next.val < nodeToInsert.val:
                    nodePreToInsert = nodePreToInsert.next
                head.next = nodeToInsert.next
                nodeToInsert.next = nodePreToInsert.next
                nodePreToInsert.next = nodeToInsert
            else:
                head = head.next
        return dummy_head.next
#O(n square) time and O(1) space