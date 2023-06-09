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


        """
        [0, 1]
        adj = {}
        degree = {1:0, 0:1}
            Adj should be an adjacency list where the key = prereq, value = all nodes that have prereq as a prereqisite

        After putting 1 into the result array should reduce the degree of 0 to 1 because that is the nodes that 1 is a prerequisite for 
        Result should be [1, 0]
        So 1 is initially a source because it does not depend on anything 
        After putting in 1, should be a way to 

        degree = {0:0, 1:1} Any time a course requires another course as a prerequisite increase its degree
        prereq = {0:[1], 1:[]} Key should be a prereq for each element in the value list 
        """
        degree = collections.defaultdict(int)
        adj = collections.defaultdict(list)

        for node, prereq in prerequisites:
            degree[node]+=1
            adj[prereq].append(node)

        # print(degree)
        # print(adj)

        sources = collections.deque()
        for node in range(numCourses):
            if degree[node] == 0:
                sources.append(node)
            
        res = []
        while sources:
            top = sources.popleft()
            res.append(top)
            for element in adj[top]:
                degree[element] -= 1
                if degree[element] == 0:
                    sources.append(element)
        
        if len(res) != numCourses:
            return []
        return res
        """
        prerequisites = [[1,0]]
        degree = {1:1, 0:0}
        adj = {1:[], 0:[1]}
        sources = [0]
        res = [0]
        """