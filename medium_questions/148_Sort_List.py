# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. Convert list to array
        2. Sort array
        3. Generate new list
        
        n = len(list)
        time: O(nlogn)
        space = O(n) -> O(1)
        
        4 -> 2 -> 1 -> 3
                            h
        
        saved = [4, 2, 1, 3]
        
        saved = [1, 2, 3, 4]
                    e
        1 -> 2 -> 3 -> 4      
        r
                          c
         
        """
        saved = []
        while head:
            saved.append(head.val)
            head = head.next
        
        saved.sort()
        
        res = None
        cur = None
        
        for e in saved:
            if not res:
                res = ListNode(e)
                cur = res
            else:
                cur.next = ListNode(e)
                cur = cur.next
                
        return res
            