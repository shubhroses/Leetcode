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
