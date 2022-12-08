class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        Take the 4 first nodes
        Return a dupicate
        """
        nodes = [edges[0][0], edges[0][1], edges[1][0], edges[1][1]]

        visited = set()
        
        for n in nodes:
            if n in visited:
                return n
            visited.add(n)