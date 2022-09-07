class OrderedStream:

    def __init__(self, n: int):
        self.saved = [None]*n
        self.l = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.saved[idKey-1] = value
        
        res = []
        while self.l < len(self.saved) and self.saved[self.l]:
            res.append(self.saved[self.l])
            self.l += 1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)