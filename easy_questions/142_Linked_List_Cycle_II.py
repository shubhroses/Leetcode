# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def calculate_cycle_length(slow):
            current = slow
            cycle_length = 0

            while True:
                current = current.next
                cycle_length += 1
                if current == slow:
                    break
            return cycle_length

        def find_start(head, cycle_length):
            pointer1 = head
            pointer2 = head

            while cycle_length > 0:
                pointer2 = pointer2.next
                cycle_length -=1
            
            while pointer1 != pointer2:
                pointer1 = pointer1.next
                pointer2 = pointer2.next
            return pointer1
        
        
        
        cycle_length = 0

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                cycle_length = calculate_cycle_length(slow)
                break

        """
        Step 1:
            Find a cycle using fast low pointer
        Step 2:
            Starting at slow follow list until list hits slow again maintaining cycle length
        Step 3:
            Using cycle length instatiate two pointers
            Move pointer 2 cycle_length times ahead
            Since the cycle add cycle_length nodes to the list, if we increment p2 cycle_length times, then increment both p1 and p2 until they meet it will be at start of the node. 
        """
        
        if cycle_length == 0:
            return None
        return find_start(head, cycle_length)