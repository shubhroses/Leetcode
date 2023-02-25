class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)

        heap = []
        heapq.heapify(heap)

        for char, count in c.items():
            heapq.heappush(heap, (-1*count, char))

        res = ""

        while heap:
            count, char = heapq.heappop(heap)
            res += char*(-1*count)
        return res

        """
Issues:
    Remember that heapq is automatically a min heap
    So to get max values have to enter -1*val every time
        """