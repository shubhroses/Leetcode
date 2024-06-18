class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Start a bfs/dfs from node k 
        Want to find length of longest path 
        
        When adding elements to an adjacency list, and accessing them later remember the order. For dijkstra you need a min heap and visited set.
        """
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
            
        minHeap = [(0, k)]
        heapq.heapify(minHeap)
        
        visit = set()
        
        t = 0
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)
            
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w2 + w1, n2))
                    
        if len(visit) != n:
            return -1
        return t