class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        for i in range(len(matrix)):
            heapq.heappush(minHeap, [matrix[i][0], 0, matrix[i]])
        
        numberCount, number = 0, 0

        while minHeap:
            number, i, row = heapq.heappop(minHeap)
            numberCount += 1
            if numberCount == k:
                break
            if len(row) > i + 1:
                heapq.heappush(minHeap, [row[i+1], i+1, row])
        return number