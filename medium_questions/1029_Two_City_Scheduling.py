class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        2 cities a and b
        2n people 
        Want n people in each city 
        
        costs = [[10, 20], [30, 50]]
                     i
        A = 1
        B = 1
        
        takeA: + 10
            costs = [[10, 20], [30, 50]]
                                    i
            A = 0
            B = 1
            
            takeB: + 50
            
            costs = [[10, 20], [30, 50]]
                                           i
            
            A = 0
            B = 0
        = 60
        
        takeB = 

        """
        
        """
        1. Sort costs by gain which company has by sending a person to city A and not to city B
        2. Send first n people to A and next n to b
        
        if you send in other way its max cost
        """
        costs.sort(key = lambda x : x[0]-x[1])
        
        total = 0
        n = len(costs)//2 #Since this returns an int
        for i in range(n):
            total += costs[i][0] + costs[n + i][1]
        return total
        
        
        
        
        dp = {}
        def helper(i, A, B):
            if (i, A, B) in dp:
                return dp[(i, A, B)]
            if i == len(costs):
                return 0
            if A == 0:
                return helper(i+1, A, B-1) + costs[i][1]
            if B == 0:
                return helper(i+1, A-1, B) + costs[i][0]
              
            #Take city A
            takeA = helper(i+1, A-1, B) + costs[i][0]
            takeB = helper(i+1, A, B-1) + costs[i][1]
            
            dp[(i, A, B)] = min(takeA, takeB)
            return dp[(i, A, B)]
        n = len(costs)
        return helper(0, n/2, n/2)
    
        """
        Where am I doing work 
        
        if the current min is already greater an the min we have its useless work. 
        
        helper(x, y, z)
        """
    