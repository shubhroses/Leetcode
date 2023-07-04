import heapq
class MinStack:
    
    """
    l = [5]
    h = [3, 4, 5]
    v = {5: 1}
    """

    def __init__(self):
        self.l = []
        self.h = []
        self.v = {}
        
    def push(self, val: int) -> None:
        self.l.append(val)
        self.v[val] = self.v.get(val, 0) + 1
        heapq.heappush(self.h, val)

    def pop(self) -> None:
        top = self.l[-1]
        self.l.pop()
        if top == self.h[0]:
            heapq.heappop(self.h)
        self.v[top] -= 1
        if self.v[top] == 0:
            del self.v[top]
        
    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        mn = self.h[0]
        while mn not in self.v:
            mn = heapq.heappop(self.h)
        return mn

# Using a stack
class MinStack:
    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:

        self.s.append((val, min(self.getMin(), val)))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        if self.s:
            return self.s[-1][1]
        return float("inf")
    

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        value = val
        if self.minStack:
            value = min(self.minStack[-1], val)
        self.minStack.append(value)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]