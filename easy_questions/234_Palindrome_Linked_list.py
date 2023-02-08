# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        1. Find middle node
        2. Reverse Second half
        3. Compare first half with reversed second half
        4. Reverse second half of the linkedlist

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
            return True
        
        # Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse Second half
        head_second_half = reverse(slow)
        copy_head_second_half = head_second_half

        while head is not None and head_second_half is not None:
            if head.val != head_second_half.val:
                break
            
            head = head.next
            head_second_half = head_second_half.next
        
        # Reverse second half
        reverse(copy_head_second_half)

        if not head or not head_second_half:
            return True

        return False