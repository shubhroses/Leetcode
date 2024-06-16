class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        For each node find the distance to the closest node, from that node find the distance to the closest available node

        res = 0

        allNodes = points

        1. Create an adj list 
            key = point (x, y), value = [neighbors (x,y)]
        2. 

              e
                 d
              b     c

        a

        adj = {
            a: [b, d, e, c],
            b: [a, e, d, c],
            d: [a, b, e, c],
            c: [a, b, d, e],
            e: [a, b, c, d],   
            }

        cost = 0

        dist(x1, y1, x2, y2):

        starting a points[0]

        visited = {}
        minHeap = [(0, points[0])]

        while len(visited) < len(points) - 1:
            pop from heap
            if top of heap in visited:
                continue
            visited.add(top of heap)
            cost += cost of top of heap
            for all elments in adj[top of heap]
                add to minheap (dist(top of heap, element), element)
        return res
        

        visited = {}
        minHeap = [(2, b), (9, d) ...  ]
        c, t = 0, a
        cost = 0

        points: List[List[int]]
        """
        adj = collections.defaultdict(list)
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                adj[(x1, y1)].append([x2, y2])
        

        def dist(x1, y1, x2, y2):
            return abs(x1-x2) + abs(y1 - y2)
        
        cost = 0
        visited = set()
        minHeap = [(0, points[0])]
        heapq.heapify(minHeap)

        while len(visited) <= len(points) - 1:
            c, top = heapq.heappop(minHeap)
            if (top[0], top[1]) in visited:
                continue
            visited.add((top[0], top[1]))
            cost += c
            for neigh in adj[(top[0], top[1])]:
                heapq.heappush(minHeap, (dist(neigh[0], neigh[1], top[0], top[1]), neigh))
        return cost





        
        






























        
