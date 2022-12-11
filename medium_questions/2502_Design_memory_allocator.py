class Allocator:

    def __init__(self, n: int):
        self.arr = [False] * n
        self.N = n
        self.map = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        count = 0
        for right in range(self.N):
            if self.arr[right]:
                count += 1
            if right >= size and self.arr[right-size]:
                count-=1 # Count number of trues in previous window of size size
            if count == 0 and right + 1 >= size:
                self.map[mID].append((right-size + 1, size))
                for x in range(right - size + 1, right + 1):
                    self.arr[x] = True
                return right - size + 1
        return -1
            

        
    def free(self, mID: int) -> int:
        t = 0
        for x, s in self.map[mID]:
            for i in range(x, x+s):
                self.arr[i] = False
                t += 1
        del self.map[mID]
        return ts