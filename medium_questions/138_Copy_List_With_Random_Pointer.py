"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        1. Create head
        2.1 maintain set of visited nodes, 
        2.2 If head.next or head.random created, just add pointer Create head.next and head.random
        
        maintain set of visited nodes, 
        
        mp {ogNode:newNode}
        
        if cur in mp: Means we have already created a node and all we need to do is point to mp[node]
        else: Need to create the node and add it to mp
        
        head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
                                 curr
        temp = [[0, null], [7, null], [13,0], [11, 4], [10,2]]
        
        mp = {[7,null]:[7,null], [13, 0]:[13, 0], [11, 4]:[11, 4], [10,2]:[10,2]}
        
        Check cur in mp:
        while cur:
            Check cur.next and cur.next in mp
            Check cur.random and cur.random in mp
            cur = cur.next
                
        since cur not in mp: 
            1. Create new node
            2. 
        
        """
        if not head:
            return None
        
        mp = {}
        temp = Node(0)
        temp.next = Node(head.val)
        cur = temp.next
        mp = {head:cur}
        while head:
            if head.next:
                if head.next in mp: #We have already visited head.next
                    cur.next = mp[head.next]
                else:
                    cur.next = Node(head.next.val)
                    mp[head.next] = cur.next
                if head.random in mp:
                    cur.random = mp[head.random]
                else:
                    if head.random:
                        cur.random = Node(head.random.val)
                    else:
                        cur.random = None
                    mp[head.random] = cur.random
            else:
                if head.random:
                    cur.random = mp[head.random]
                else:
                    cur.random = None
            cur = cur.next
            head = head.next
        return temp.next
            
        """       h               c
    index:    0   1           0   1   2
    val:      1   2           1   2
    next:     1   None        1   None
    random:   1   1           1   1
    
    
        mp = {0:0, 1:1}
        
        temp =
        
        """
        """
        Neetcode solution
        """
        old = {None:None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            old[cur] = copy
            cur = cur.next
            
        cur = head
        while cur:
            copy = old[cur]
            copy.next = old[cur.next] 
            copy.random = old[cur.random] 
            cur = cur.next
        
        return old[head]