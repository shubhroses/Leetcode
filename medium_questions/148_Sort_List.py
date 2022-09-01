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
            
        #Neet code solution
        def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next
        
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Base case
        if not head or not head.next:
            return head
        
        #Split the list into two halves
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        #Keep splitting until one node left
        left = self.sortList(left)
        right = self.sortList(right)
        
        #Combined split up elements
        return self.merge(left, right)
        
        """
        Merge Sort:
        
        4 -> 2 -> 1 -> 3 -> 
        
        4 -> 2 ->
        1 -> 3 -> 
        
        4 ->
        2 ->
        1 ->
        3 ->
        
        2 -> 4 -> 
        1 -> 3 -> 
        
        1 -> 2 -> 3 -> 4 -> 
        """