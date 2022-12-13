class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(current, previous):
            count = 1
            for neighbor in graph[current]:
                if neighbor == previous:
                    continue
                count += dfs(neighbor, current)
            if current != 0:
                self.ans += math.ceil(count / seats)
            return count
        
        self.ans = 0
        dfs(current = 0, previous = -1)
        return self.ans
       