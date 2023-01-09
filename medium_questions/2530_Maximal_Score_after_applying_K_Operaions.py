class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        """
        Put all numbers in a max heap
        Maintain res
        
        """
        nums = [-1*i for i in nums]
        heapq.heapify(nums)
        res = 0
        
        for _ in range(k):
            top = abs(heapq.heappop(nums))
            res += top
            heapq.heappush(nums, -math.ceil(top/3))
        return res