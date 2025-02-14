class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        heapq.heapify(self.heap)
        self.k = k

        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        

"""
Issues:
    The kth largest element in the sorted order can be found by keeping a max heap and returning the heap[0] element in the end

    The kth smallest element can be found by return -1*heap[0] while adding -1*num to heap 
I"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k

        for n in nums:
            if len(self.h) < k:
                heapq.heappush(self.h, n)
            else:
                if n > self.h[0]:
                    heapq.heappop(self.h)
                    heapq.heappush(self.h, n)

        
    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        elif val > self.h[0]:
            heapq.heappop(self.h)
            heapq.heappush(self.h, val)
        

        return self.h[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

"""
Maintain a max heap of size k



[4, 5, 8, 2]
 i


h = [4, 5, 8]

since 2 is not > 4 dont do anything
but if 6 comes
pop from heap 
append to heap 
and reheapify


"""