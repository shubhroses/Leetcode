class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        """
        Build obstacle at (x, y)
        find distance of kth nearest obstacle to the origin

        maintain a max heap that can have a maximum of k elements in it
        after each query if val < top of heap. Pop form heap an dput in new elemnt

        queries = [[1,2],[3,4],[2,3],[-3,0]], k = 2
                    x y
        dist = 3
        heap = [(-1, [1, 2])]
        res = []

        3275_Kth_nearest_obstacle_queries.py
        """

        heap = []

        res = []
        for x, y in queries:
            dist = abs(x) + abs(y)
            heapq.heappush(heap, (-1 * dist, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)
            if len(heap) < k:
                res.append(-1)
            else:
                res.append(-1 * heap[0][0])
        
        return res