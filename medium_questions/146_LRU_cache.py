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