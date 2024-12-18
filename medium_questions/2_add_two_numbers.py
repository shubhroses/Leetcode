# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        While both
        l1 + l2 + rem

        create node with last digit of rem, update rem


        while l2 
        add l2 + rem

        while l1
        add l1 + rem


        
        2 -> 4 -> 3 -> 1
        l1

        5 -> 6 -> 4
        l2

        d -> 7 
             c

        rem = 0

        """
        dummy = ListNode()
        cur = dummy

        rem = 0

        while l1 and l2:
            tot = l1.val + l2.val + rem

            lastDigit = int(str(tot)[-1])

            if len(str(tot)) > 1:
                rem = int(str(tot)[:-1])
            else:
                rem = 0
            
            newNode = ListNode(val = lastDigit)
            cur.next = newNode
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        

        while l1:
            tot = l1.val + rem

            lastDigit = int(str(tot)[-1])

            if len(str(tot)) > 1:
                rem = int(str(tot)[:-1])
            else:
                rem = 0
            
            newNode = ListNode(val = lastDigit)
            cur.next = newNode
            cur = cur.next
            l1 = l1.next

        
        while l2:
            tot = l2.val + rem

            lastDigit = int(str(tot)[-1])

            if len(str(tot)) > 1:
                rem = int(str(tot)[:-1])
            else:
                rem = 0
            
            newNode = ListNode(val = lastDigit)
            cur.next = newNode
            cur = cur.next
            l2 = l2.next
        

        if rem:
            newNode = ListNode(val = rem)
            cur.next = newNode


        return dummy.next
