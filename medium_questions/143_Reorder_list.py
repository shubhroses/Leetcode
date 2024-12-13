# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        1. Find middle 
        2. Reverse second half
        3. Interleave
        """
        def reverse(head):
            prev = None
            while head:
                next = head.next
                head.next = prev
                prev = head
                head = next
            return prev


        if not head or not head.next:
            return

        # Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse Second Half
        head_second_half = reverse(slow)
        head_first_half = head

        # Interleave
        
        while head_first_half and head_second_half:
            temp = head_first_half.next
            head_first_half.next = head_second_half
            head_first_half = temp

            temp = head_second_half.next
            head_second_half.next = head_first_half
            head_second_half = temp
        
        if head_first_half:
            head_first_half.next = None
        
        
        
        return head
        
        
        class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        1 -> 2 -> 3 -> 4 -> 5
                  s 
                                f
        """
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            
        l1 = head
        l2 = slow.next
        slow.next = None

        def reverseList(start):
            prev = None
            cur = start

            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev
        
        l2 = reverseList(l2)

        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            cur.next = l1
            l1next = l1.next
            cur = cur.next
            l1 = l1next

            cur.next = l2
            l2next = l2.next
            cur = cur.next
            l2 = l2next
        
        if l1:
            cur.next = l1

        return dummy.next
        