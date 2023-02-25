class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Brute force:
            Sort, take k from end element
            
        [3,2,1,5,6,4] k = 2
        [1,2,3,4,5,6] n = 6
        
        nums[n-k] = nums[4]
        """
        # return sorted(nums)[len(nums)-k]
        
        """
        Create heap from nums
        Pop k times
        
        o(n) to create
        o(klogn) to pop k times
        """
        # heapq.heapify(nums)
        # res = None
        # for _ in range(len(nums) - k + 1):
        #     res = heapq.heappop(nums)
        #     print(res)
        # return res
    
        # Quick Select
        if not nums: 
            return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
        
        """
        1. If not nums return 
        2. Choose a random pivot
        3. Separate nums into left, mid, and right
        4. If k < length of less than elements, do quick select on left array
        5. If k > length of equal to and greater than, do quick select on right array
        6. Return first mid other wise. 
        """
        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for num in nums:
            # print(heap)
            heapq.heappush(heap, num)
            while len(heap) > k:
                top = heapq.heappop(heap)
                # print("popped :", top)
        return heap[0]