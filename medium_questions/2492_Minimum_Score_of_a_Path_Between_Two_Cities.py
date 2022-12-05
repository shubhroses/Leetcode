global res
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graphs = defaultdict(list)
        costs = {}
        
        for i, j, cost in roads:
            graphs[i].append(j)
            graphs[j].append(i)
            
            costs[(i, j)] = cost
            costs[(j, i)] = cost
        """
        Find out if 1 and n are connected 
        """
        global res
        res = inf
        connected = set([1])
        
        visited = set()
        def dfs(i):
            global res
            if i in visited:
                return
            visited.add(i)
            for neigh in graphs[i]:
                res = min(res, costs[(i, neigh)])
                connected.add(neigh)
                dfs(neigh)
                
        dfs(1)
        return res