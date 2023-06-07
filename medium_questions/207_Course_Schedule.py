class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        prerequesites[i] = [ai, bi]
            must take bi before ai 
        
        [0, 1] -> have to take 1 before 0
        
        0 -> 1
        
        [0, 1]
        {0: [1]}
        
        [a, b]
        {a: [b]}
        
        
        {0: [1],
         1: [2],
         2: [0]}
         
        checkCycle(2):
            visited.add(2)
            
        visited = {0, 1, 2, 0}
         
        
        0 -> 1 -> 2 -> 0, when you have a cycle cant complete all courses 
        
        1. Create adjacency list
            {0: [1]}
            course 0 depends on course 1
            can only get to course 0 if we first get to course 1. 
            
            Iterate through all node
                for all other nodes that it is dependet on iterate through them 
                
            {node: [all other nodes it is dependent on]}
        
        Want to return False
        {0: [1],
         1: [2],
         2: [0]}
         
        visited = {0, 1, 2, 0}
        
        {0: [1]}
        checkCycle(0)
        
        visited = {}
        
        
        """
        
        adj = collections.defaultdict(list)
        for [a, b] in prerequisites:
            adj[a].append(b)
        
        visited = set()
        accepted = set()
        
        def checkCycle(course):
            if course in accepted:
                return False
            if course in visited:
                return True
            visited.add(course)
            for pre in adj[course]:
                if checkCycle(pre):
                    return True
            visited.remove(course)
            accepted.add(course)
            return False
        
        for course in range(numCourses):
            if checkCycle(course):
                return False
        return True

        # Neetcode solution

        adj = {i:[] for i in range(numCourses)}
        for [a, b] in prerequisites:
            adj[a].append(b)
        
        visited = set()
        
        
        def checkCycle(course):
            if course in visited:
                return True
            if adj[course] == []:
                return False
            visited.add(course)
            for pre in adj[course]:
                if checkCycle(pre):
                    return True
            visited.remove(course)
            adj[course] = []
            return False
        
        for course in range(numCourses):
            if checkCycle(course):
                return False
                
        return True
    class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        1. Create an adjacency list 
            key = node
            value = list of nodes that are prerequisites
        2. Write a DFS function
            Function determines weather a course can be completed
            Base case: If the value is empty than can be completed
            If all prerequisites can be completed that can be completed
        3. For each course call the dfs function
            Maintain a visited set so that while doing dfs, if reach an already visited node there is a cycle and can return false
        """
        adj = collections.defaultdict(list)
        for node, prereq in prerequisites:
            adj[node].append(prereq)

        visited = set()
        def dfs(node):
            if not adj[node]:
                return True
            if node in visited:
                return False
            visited.add(node)
            for prereq in adj[node]:
                if not dfs(prereq):
                    return False
            visited.remove(node)
            adj[node] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            