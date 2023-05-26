class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for neigh in adj[node]:
                dfs(neigh)


        for e in range(n):
            if e in visited:
                continue
            dfs(e)
            res += 1
        return res