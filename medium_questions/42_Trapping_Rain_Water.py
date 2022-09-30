class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Iterate level by level
        Go through whole level
        
        level 1:
        l = left most bar of height >= 1
        r =  right most bar of height >= 1
        
        iterate c from l to r:
            if c <= level:
                count += 1
                
        Iterate from right to left maintaining the bar height, 
        [0, 1, 0, 1, 2, 1, 0, 1, 2, 1, 2]
        [2, 3, 1, 2, 3, 2, 0, 0, 1, 0, 0]
        
        [0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0]
        
        maxHeight = 1
        cur = 0
        
        add maxHeight-cur
        
        maxHeight = max(cur, maxHeight)
        
        Iterate from left to right maintiaing bar height,
        []
        
        """
        
        leftToRight = [0]*len(height)
        maxHeight = 0
        for i in range(len(height)):
            cur = height[i]
            maxHeight = max(cur, maxHeight)
            leftToRight[i] = maxHeight-cur
        
        rightToLeft = [0]*len(height)
        maxHeight = 0
        for i in range(len(height)-1, -1, -1):
            cur = height[i]
            maxHeight = max(cur, maxHeight)
            rightToLeft[i] = maxHeight-cur
            
        for i in range(len(height)):
            rightToLeft[i] = min(rightToLeft[i], leftToRight[i])
            
        return sum(rightToLeft)
            