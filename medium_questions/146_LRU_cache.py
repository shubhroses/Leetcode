class DLinkedListNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {} # key : node
        
        self.head= DLinkedListNode()
        self.tail = DLinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def _add_to_head(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
    
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)
        
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res
        
    
    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if not node:
            newNode = DLinkedListNode()
            newNode.key = key
            newNode.value = value
            
            self.cache[key] = newNode
            self._add_to_head(newNode)
            self.size += 1
            
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -=1
        else:
            node.value = value
            self._move_to_head(node)


class DLNode:
    def __init__(self):
        self.key = None
        self.value = None
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # Doubly linked list node 
        self.head = DLNode()
        self.tail = DLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # Map to maintain elements 
        # {key : node(key, value)}
        self.dict = {}
        
        
        # Capacity
        self.capacity = capacity
        self.count = 0
        
    def addToHead(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        
        self.head.next = node
        node.prev = self.head
        
        """
        head -> tail
             <-
             
        head -> node -> tail
             <-      <-
        """
        
    def popFromTail(self):
        """
        head -> node -> tail
             <-      <-
        """
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return node
        
    def removeFromList(self, node):
        """
        head -> node -> tail
             <-      <-
        """
        node.prev.next = node.next
        node.next.prev = node.prev 
        
    def moveToHead(self, node):
        self.removeFromList(node)
        self.addToHead(node)
        
        
    def get(self, key: int) -> int:
        
        # print(key, self.dict[key].value)
        node = self.dict.get(key, None)
        if not node:
            return -1
        self.moveToHead(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            # Update value of key
            self.dict[key].value = value
            node = self.dict[key]
            self.removeFromList(node)
            self.addToHead(node)
        else:
            # key not in dictionary 
            """
            1. Create new node with value
            2. If count == capacity
                Remove from tail
            3. Else 
                Add to head
            """
            newNode = DLNode()
            newNode.value = value
            newNode.key = key
            self.dict[key] = newNode
            self.count += 1
            self.addToHead(newNode)
            if self.count > self.capacity:
                removeNode = self.popFromTail()
                del self.dict[removeNode.key]
                del removeNode
                self.count -=1
                
            



            
             
        

"""
Maintain map to allow get

Add key-value to cache using put if not already in, if number of keys exceeds the capacity, evict the least recently used key 

Add to head 
Pop from tail
Remove form list 
"""

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    Need capacity and used as varaible
    Map for key to value 
    If key exists update Map
    if key does not exist add to map and 
    to head of doubley linked list
    if used > capacity, remove from tail of linked list

    h <=> t

    5

    h <-> 5 <-> t
    """
    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.used = 0

        self.map = {}
        
    def get(self, key: int) -> int:
        """
        Figure out node, so map should store node
        """
        if key in self.map:
            value = self.removeFromMiddle(key)
            self.addToHead(key, value)
            return value
        return -1
    
    def removeFromMiddle(self, key):
        nodeToDel = self.map[key]
        prevNode, nextNode = nodeToDel.prev, nodeToDel.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
        res = nodeToDel.value
        del self.map[key]
        return res
    
    def addToHead(self, key, value) -> None:
        newNode = ListNode(key, value)
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode
        newNode.prev = self.head

        self.map[key] = newNode
    
    def removeFromTail(self) -> None:
        lastNodeKey = self.tail.prev.key

        newLast = self.tail.prev.prev
        newLast.next = self.tail
        self.tail.prev = newLast

        del self.map[lastNodeKey]
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.removeFromMiddle(key)
            self.addToHead(key, value)
            return
        
        if self.used == self.capacity:
            # Add to head
            self.addToHead(key, value)

            # remove from tail
            self.removeFromTail()
            
        else:
            # Add to head
            self.addToHead(key, value)
            self.used += 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

