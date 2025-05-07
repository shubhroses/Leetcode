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
        
        
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Maintain a max heap of only the k closest elements

        If the next element is smaller than top of heap than pop from heap and append the new element 
        """
        h = []
        for x, y in points:
            distance = (x**2 + y**2)**(1/2)
            if len(h) < k:
                heapq.heappush(h, (-1 * distance, [x, y]))
            else:
                top_dist = -1 * h[0][0]
                if distance < top_dist:
                    heapq.heappop(h)
                    heapq.heappush(h, (-1 * distance, [x, y]))
        return [i[1] for i in h] 