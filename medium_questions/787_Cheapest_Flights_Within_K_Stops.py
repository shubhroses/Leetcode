class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Find all paths from src to dst
        Find only keep paths of length less than k stops
        Return the path with lowest weight

        length of path - 2 can't be greater than k  

        res = inf

        graph = {0:[(1, 100)], 
                 1:[(2, 100)],
                 2:[(0, 100), (3, 200)],
                 3:[]}

        1. Create graph
        2. Create heap with ()weight, node, length)
        3. Do bfs but instead of queue use heap
            4. pop
            5. If reached destination return weight
            6. If k > 0
                for every neighbor
                    add to heap (price + new price, neighbor, k - 1)
        """
        visited = {}
        graph = collections.defaultdict(list)
        for s, d, p in flights:
            graph[s].append((d, p))
        heap = [(0, 0, src)]
        while heap:
            dist, moves, node = heapq.heappop(heap)
            if node == dst and k >= moves - 1:
                return dist
            if node not in visited or visited[node] > moves:
                visited[node] = moves
                for nei, weight in graph[node]:
                    heapq.heappush(heap, (dist + weight, moves + 1, nei))
        return -1