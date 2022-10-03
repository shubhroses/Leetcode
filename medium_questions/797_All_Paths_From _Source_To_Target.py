class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Do dfs from the start node until you reach end
        
        [0: [1,2],
         1: [3],
         2: [3],
         3: []]
        
        i = 0
        path = [0, 1, 3]
        """
        
        
        res = []
        
        def dfs(i, path):
            if i == len(graph)-1:
                path = path + [i]
                res.append(path)
                return
            for neigh in graph[i]:
                dfs(neigh, path + [i])
        
        dfs(0, [])
        return res