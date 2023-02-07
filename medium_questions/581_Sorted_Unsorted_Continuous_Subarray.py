class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Find a window where max of window is less than right value and min of window is greater than left value
        put all the numbers in a min and max heap

        have a left and right pointer
        if left is at top of min heap, pop heap and increment l
            continue
            
        """
        low, high = 0, len(nums)-1

        while low < len(nums) -1 and nums[low] <= nums[low+1]:
            low+=1
        
        if low == len(nums)-1:
            return 0

        while high > 0 and nums[high] >= nums[high-1]:
            high -=1

        subnumsay_max = max(nums[low:high+1])
        subnumsay_min = min(nums[low:high+1])

        while low > 0 and nums[low-1] > subnumsay_min:
            low-=1
        while high < len(nums)-1 and nums[high+1] < subnumsay_max:
            high += 1

        return high - low + 1


        """ minHeap = nums.copy()
        heapq.heapify(minHeap)

        maxHeap = [n * -1 for n in nums]
        heapq.heapify(maxHeap)

        l = 0
        while l < len(nums):
            if nums[l] == minHeap[0]:
                heapq.heappop(minHeap)
                l+=1
            else:
                break

        r = len(nums)-1
        while r >= 0:
            if nums[r]*-1 == maxHeap[0]:
                heapq.heappop(maxHeap)
                r-=1
            else:
                break
        
        if r < l:
            return 0
        return r-l+1"""