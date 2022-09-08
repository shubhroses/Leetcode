class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Run a dfs starting at each node.
        Every time you run dfs on an unvisited node increment counter
        Any time you visit a node, add it to visited set
        
           0 1 2
        0 [1,1,0]
        1 [1,1,0]
        2 [0,0,1]
        
        
        i = 0
        visited = {0, 1}
            
        
        """
        visited = set()
        res = 0
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not j in visited:
                    visited.add(j)
                    dfs(j)
        
        for i in range(len(isConnected)):
            if not i in visited:
                dfs(i)
                res+=1
        return res
        