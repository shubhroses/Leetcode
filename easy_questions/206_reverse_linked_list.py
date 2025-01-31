# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1 -> 2 -> 3 -> None
    p.  h
    
        """
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
        
        p, c = None, head
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        return p
        