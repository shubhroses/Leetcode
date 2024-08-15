class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        prev = dummy
        cur = head
        
        while cur and cur.next:
            # Nodes to be swapped
            first = cur
            second = cur.next
            
            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Reinitializing the pointers
            prev = first
            cur = first.next
        
        return dummy.next
        # 24_swap_nodes_in_pairs.py
