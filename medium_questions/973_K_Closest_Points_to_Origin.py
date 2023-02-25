class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return math.sqrt(x**2 + y**2)

        maxHeap = []
        heapq.heapify(maxHeap)

        for i in range(k):
            x,y = points[i]
            heappush(maxHeap, (-1*distance(x, y), points[i]))
        
        for i in range(k, len(points)):
            x,y = points[i]
            dist = distance(x, y)
            if -1 * dist > maxHeap[0][0]:
                heappop(maxHeap)
                heappush(maxHeap, (-1*dist, points[i]))
        return [maxHeap[i][1] for i in range(len(maxHeap))]