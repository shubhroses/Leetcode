class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        Read question carefully
        Start with a simple example 
        
        
        [1, 2, 3, 2, 1] 
                  i
        mx = 1
        res = [2, 3, 4]
        
        [3, 2, 1]
         i
        mx = 2
        res = [2, 1, 0]
        
        [0, 1, 2]
        
          i
        i i i
        
        mx = 0
        
        [1, 2, 1]
         i
        mx = 2
        res = [2, 1]
        """
        mx = 0
        res = []
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > mx:
                res.append(i)
                mx = heights[i]
        return reversed(res)