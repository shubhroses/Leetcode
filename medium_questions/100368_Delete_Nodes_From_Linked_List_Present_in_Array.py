# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numsSet = set(nums)
        saved = ListNode()
        saved.next = head


        prev = saved
        cur = head

        while cur:
            if cur.val in numsSet:
                prev.next = cur.next
                cur = prev.next
            else:
                cur = cur.next
                prev = prev.next
        return saved.next
        """
        consider no list or only one element
        nums = [5]

        s
        p    c
          -> 1 -> None
        """
# 100368_Delete_Nodes_From_Linked_List_Present_in_Array.py
