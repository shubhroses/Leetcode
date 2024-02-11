class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        do bfs and if count == n then good?
        """
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for neigh in adj[node]:
                if neigh == prev:
                    continue
                if not dfs(neigh, node):
                    return False
            return True
        
        validTree = dfs(0, -1)
        if len(visited) == n and validTree:
            return True
        return False

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        queue = collections.deque([0])

        parent = [-1]*n

        while queue:
            for _ in range(len(queue)):
                top = queue.popleft()
                visited.add(top)

                for neigh in adj[top]:
                    if neigh not in visited:
                        parent[neigh] = top
                        queue.append(neigh)
                    elif neigh != parent[top]: # There is a cucle is neigh in visited and neigh is not parent
                        return False
        return len(visited) == n