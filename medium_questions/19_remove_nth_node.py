# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
         c       i    
               

        dummy -> 1 -> 2 -> None
           
         c       i    
        n = 1

        dummy -> 1  -> None
           
         c              i    
        n = 1
                           

        Push i n times

        while i:
            push c and I
            c.next = c.next.next
        
        """

        dummy = ListNode()
        dummy.next = head

        c, i = dummy, head

        for _ in range(n):
            if not i:
                return head
            i = i.next
        
        while i:
            c = c.next
            i = i.next
        
        c.next = c.next.next

        return dummy.next

        
