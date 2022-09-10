class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        prerequesites[i] = [ai, bi]
        a -> b
        
        1. create adjacency list
        2. Do breath first search on each course
        3. As you see course add to res
        """

        adj = {i:[] for i in range(numCourses)}
        for [a, b] in prerequisites:
            adj[a].append(b)
            
        res = []
        
        cycle = set()
        visited = set()
        
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            
            cycle.add(node)
            
            for neigh in adj[node]:
                if not dfs(neigh):
                    return False
                
            cycle.remove(node)
            visited.add(node)
            res.append(node)

            return True
            
        
        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return res