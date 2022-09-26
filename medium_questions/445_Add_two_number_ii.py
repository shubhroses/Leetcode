# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterate through l1 to get num 1
        Iterate through l2 to get num 2
        
        Add them 
        
        Create new linked list
        """
        def reverseList(head):
            if not head:
                return None
        
            temp = None
            while head.next:
                saved = head.next
                head.next = temp
                temp = head
                head = saved
            head.next = temp
            return head
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        
        head = None
        carry = 0
        while l1 or l2:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            
            val = (carry + x1 + x2) % 10
            carry = (carry + x1 + x2) // 10
            
            curr = ListNode(val)
            curr.next = head
            head = curr
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr
        return head