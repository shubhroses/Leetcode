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