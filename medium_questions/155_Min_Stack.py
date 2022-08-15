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