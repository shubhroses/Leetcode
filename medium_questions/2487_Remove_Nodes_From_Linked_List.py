# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        def reverseList(helperhead):
            # Reverse a linked list 
            temp = helperhead
            cur = temp.next
            temp.next = None

            while cur:
                new = cur.next
                cur.next = temp
                temp = cur
                cur = new

            return temp
        
        curMin = 0
        newHead = reverseList(head)
    

        """
        1       <-      2       <-      3    -> None
   <-  temp     cur
        """
        cur = newHead
        prev = ListNode()
        prev.next = newHead
        while cur:
            if cur.val < curMin:
                # Delete node
                prev.next = prev.next.next
            else:
                curMin = cur.val
                prev = cur
            cur = cur.next
            
        return reverseList(newHead)