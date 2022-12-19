class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        """
        Find number of nodes with odd degree 
        If the number is 0, 2, 4 return True
        """
        edgesSet = set()
        
        for l, r in edges:
            edgesSet.add((l, r))
            edgesSet.add((r, l))
        
        
        nodeToDegree = {}
        for l, r in edges:
            nodeToDegree[l] = nodeToDegree.get(l, 0) + 1
            nodeToDegree[r] = nodeToDegree.get(r, 0) + 1
        
        numOdd = 0
        
        oddNode = []
        
        for node, degree in nodeToDegree.items():
            if degree % 2 == 1:
                oddNode.append(node)
        print(oddNode)
                
        if len(oddNode) not in [0, 2, 4]:
            return False
        
        if len(oddNode) == 0:
            return True
        
        if len(oddNode) == 2:
            a, b = oddNode
            
            third = False
            for c in range(1, n+1):
                if not (a, c) in edgesSet and not (b, c) in edgesSet:
                    third = True
                    break
            
            if (a, b) in edgesSet and not third:
                return False

        
        if len(oddNode) == 4:
            a, b, c, d = oddNode
            first = (a, b) not in edgesSet and (c, d) not in edgesSet
            second = (a, c) not in edgesSet and (b, d) not in edgesSet
            third = (a, d) not in edgesSet and (b, c) not in edgesSet
            
            if not (first or second or third):
                return False
        return True
        