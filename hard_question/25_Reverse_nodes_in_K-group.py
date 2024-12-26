# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev = kth.next
            curr = groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
        


    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        1. Find length of list
        2. d = Divide length by k and check for remainder
        3. For d iterations, do a switching of nodes
        4. 
          ----------->
        1 <- 2 <- 3   4 -> 5 -> 6
    d
    s   c             n
                   ----------->
       3 -> 2 -> 1   4 <- 5 <- 6
                 s             c    n

         ------------->
    d.  1 <- 2 <- 3 -> 4 -> 5 -> 6 -> None
     ------------>
    s             c.   n.   a

    
    d -> 3 -> 2 -> 1 -> 4 -> 5 -> 6 -> None
                   s    c    n
        k-1 times do a swap 
        then c.next = s.next
        s = c
        c = next
        n = c.next
        """
        if not head:
            return None
        if k == 1:
            return head
        lenList = 0
        c = head
        while c:
            c = c.next
            lenList += 1
        
        d = lenList // k

        dummy = ListNode()
        dummy.next = head
        s = dummy
        c = head
        n = head.next


        for _ in range(d):
            for _ in range(k-1):
                afterNext = n.next
                n.next = c
                c = n
                n = afterNext
            saved = s.next
            saved.next = n
            s.next = c
            s = saved
            c = n
            if c:
                n = c.next
        
        return dummy.next
        """
        k = 2
             --------->
        d    1 <- 2 -> 3 -> 4 -> 5 -> None
             sv        c.   n. 
         -------->
             s

                    --------->
        d -> 2 -> 1 -> 3 <- 4 -> 5 -> None
                       s         c.   n
                   -------->
        d -> 2 -> 1 -> 4 -> 3 -> 5 -> None
        lenList = 5
        d = 2
        """
                







    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
