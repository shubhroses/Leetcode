# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # count
        c = head
        count = 0
        while c:
            count += 1
            c = c.next
        
        if count == 0:
            return None

        rotate = k%count
        if rotate == 0:
            return head
        print("count :", count)
        print("rotate :",rotate)

        r = head
        prev = None
        while rotate > 0:
            rotate -= 1
            prev = r
            r = r.next
        
        print(f"r: {r.val}, prev: {prev.val}")

        l = head
        while r and r.next:
            l, r = l.next, r.next
            prev = prev.next
        print(f"r: {r.val}, prev: {prev.val}")
        r.next = head
        saved = l.next
        l.next = None
        return saved