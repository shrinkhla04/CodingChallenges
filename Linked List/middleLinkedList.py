#Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head 
        slow = head 
        while fast and fast.next :
            
            slow = slow.next
            fast = fast.next.next
            
        return slow
#O(n) time and O(1) space      
