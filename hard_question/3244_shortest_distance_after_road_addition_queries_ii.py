class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
		# _next[node] refers to the next node that current node points to
        _next = [i+1 for i in range(n)]
		
		# mark the last node, i.e. destination node, points to nothing
        _next[n-1] = -1
        
		# total distance from node=0 to node=n-1 is initialized as n-1
        distance = n-1
        res = []
        
        for x, y in queries:
			# Given the constraint that there will be NO queries such that queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1] 
			# ONLY 2 scenarios:
			# <----------------> query[i]
			#      <------->query[j]
			#  OR
			#      <------->query[i]
			# <----------------> query[j]
	        
            # adding x -> y path doesn't change anything
            if _next[x] == -1 or y < _next[x]:
			    # if _next[x] already points to further node (closer to destination), ignore the path
			    # or if _next[x] points to nothing, it will not affect the current shortest distance from 0 to n-1
                res.append(distance)
				
            # adding x -> path will somehow shorten the distance from 0 to n-1    
            else:
                # we can eliminate every node between x and y by marking _next[node] = -1
				# x -> _next[x] -> ... -> y
                curr = _next[x]
                while curr != y:
                    _next[curr], curr = -1, _next[curr]
                    distance -= 1 # whenever we eliminate one node, the total distance gets shortened
        
                _next[x] = y
                res.append(distance)
                
        return res
