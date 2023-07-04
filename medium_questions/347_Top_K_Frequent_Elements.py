from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())
        
        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  
            
            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]  
            
            return store_index
        
        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place. 
            """
            # base case: the list contains only one element
            if left == right: 
                return
            
            # select a random pivot_index
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return 
            # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)
         
        n = len(unique) 
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array. 
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.  
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        countNum = []

        for key, val in counter.items():
            countNum.append((val, key))
        
        countNum.sort(reverse=True)

        return [countNum[i][1] for i in range(min(k, len(countNum)))]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        # print(c)

        heap = []
        heapq.heapify(heap)

        for num, count in c.items():
            # print(heap)
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [heap[i][1] for i in range(len(heap))]
        
        """
Issues:
    When doing heappush, forget to enter heap and value
    Ensure that you are properly entering count value as first element in heap


        """
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. Make a counter from nums 
        nums = [1,1,1,2,2,3]
        c = {1:3, 2:2, 3:1}
            (count, num)
        heap: [(-3, 1), (-2, 2), (-1, 3)]

        Want to pop from heap k times
            If not heap, 

        nums = [4, 4, 5]
        c = {2:4, 1:5}

        heap = [(-2, 4), (-1, 5)]

        [4, 5]
        """
        c = {}
        for i, n in enumerate(nums):
            c[n] = c.get(n, 0) + 1
        
        h = []
        heapq.heapify(h)
        for num, count in c.items():
            heapq.heappush(h, (-count, num))

        res = []
        for _ in range(k):
            count, num = heapq.heappop(h)
            res.append(num)
        return res