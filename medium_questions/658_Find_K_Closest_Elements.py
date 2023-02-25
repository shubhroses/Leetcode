class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def binary_search(arr, target):
            low, high = 0, len(arr)-1
            while low <= high:
                mid = (high + low)//2
                if arr[mid] == target:
                    return mid
                elif arr[mid]<target:
                    low = mid + 1
                else:
                    high = mid -1
            if low > 0:
                return low -1
            return low
        index = binary_search(arr, x)
        low, high = index-k, index + k

        low = max(low, 0)
        high = min (high, len(arr)-1)

        minHeap = []
        for i in range(low, high + 1):
            heappush(minHeap, (abs(arr[i]-x), arr[i]))
        result = []

        for _ in range(k):
            result.append(heappop(minHeap)[1])

        result.sort() 
        return result    