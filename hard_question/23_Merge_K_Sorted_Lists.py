# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        I can merge two linked lists 
        
        Pair up lists and continue to merge until only one left
        
        while len(res) > 1:
        
        res = lists
        while len(res) > 1:
            res = []
            for i in range(0, len(lists), 2):
                first = lists[i]
                second = None
                if i < len(lists)-1:
                    second = lists[i+1]
                combined = mergeTwoLists(first, second)
                res.append(combined)
            
        return res[0]
        
        len(lists) = 3
        lists = [a, b, c]
                       i
        
        
        lists = [a, b]
                 i  
        lists = [a]
        
        
        1 -> 4 -> 5
                     x
        
        1 -> 3 -> 4
                      y
        
        0 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5
       res
                            cur
        """
        
        
        def mergeTwoLists(x, y): #Return merged list
            res = ListNode()
            cur = res
            while x and y:
                if x.val < y.val:
                    cur.next = ListNode(x.val)
                    x = x.next
                else:
                    cur.next = ListNode(y.val)
                    y = y.next
                cur = cur.next
            while x:
                cur.next = ListNode(x.val)
                x = x.next
                cur = cur.next
            while y:
                cur.next = ListNode(y.val)
                y = y.next
                cur = cur.next
            return res.next
        
        x = lists
        while len(x) > 1:
            temp = []
            for i in range(0, len(x), 2):
                first = x[i]
                second = None
                if i < len(x)-1:
                    second = x[i+1]
                combined = mergeTwoLists(first, second)
                temp.append(combined)
            x = temp
        if not x:
            return None
        return x[0]
        """
        x = [[1,4,5],[1,3,4],[2,6]]
        
        x = []
        """

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        backup = new_head = ListNode(0)
        Q = []
        for list_head_id,list_head in enumerate(lists):
            if list_head:
                heappush(Q,(list_head.val,list_head_id,list_head))
        while Q:
            _,list_id,new_head.next =  heappop(Q)
            new_head = new_head.next
            if new_head.next:
                heappush(Q,(new_head.next.val,list_id,new_head.next))
        return backup.next
        