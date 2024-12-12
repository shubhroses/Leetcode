# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """

        1 -> 2 -> 4 -> 5
                 l1

        1 -> 3 -> 4
                      l2

        d -> 1 -> 1 -> 2 -> 3 -> 4

                                 c

        """
        l1, l2 = list1, list2
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return dummy.next
