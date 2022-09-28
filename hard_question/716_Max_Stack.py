class linkedListNode():
    def __init__(self):
        self.val = 0
        self.next = None
        self.prev = None

class MaxStack:
    def __init__(self):
        # Create head
        # Create a heap
        # Map to maintain nodes associated with int
        self.head = linkedListNode()
        self.tail = linkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.h = []
        self.nodes = collections.defaultdict(list)
        
    def push(self, x: int) -> None:
        # Add new node with value x to head
        # Add value to heap
        # Add node to map with x as key
        newNode = linkedListNode()
        newNode.val = x
        newNode.next = self.head.next
        newNode.prev = self.head.next.prev
        self.head.next.prev = newNode
        self.head.next = newNode
        
        heappush(self.h, -x)
        self.nodes[x].append(newNode)

    def pop(self) -> int:
        # Remove first element
        # Remove from map
        first = self.head.next
        val = self.head.next.val
        
        self.head.next = first.next
        self.head.next.prev = first.prev
        del first
        self.nodes[val].pop()
        return val

    def top(self) -> int:
        # Return head.next.val
        return self.head.next.val

    def peekMax(self) -> int:
        # Return top of heap
        top = -self.h[0]
        while not self.nodes[top]:
            heappop(self.h)
            top = -self.h[0]
        return top

    def popMax(self) -> int:
        # Pop from heap
        # While value in map keep popping
        # Remove node from linked list
        
        heapTop = -heappop(self.h)
        
        while not self.nodes[heapTop]:
            heapTop = -heappop(self.h)
        node = self.nodes[heapTop][-1]
        self.nodes[heapTop].pop()
        node.prev.next = node.next
        node.next.prev = node.prev
        del node
        
        return heapTop
        
        
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

"""
Use a doubly linked list to maintain stack
use a heap of nodes to get the max



"""