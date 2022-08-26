class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        1. Brute force take all pairs of values in heights and multipfy by distance between them to get the amount of water then get max to get result 
                  l  r
        height = [1, 1]
                  0  1
        (r-l) * min(height[r], height[l])
        
        [2, 1, 3]
         l     r
        (2 - 0) * min(3, 2)
        2 * 2 = 4
        
        res = 0
        for l in range(height-1):
            for r in range(l, height):
                res = max(res, (r-l) * min(height[r], height[l]))
        return res
        
        Two pointers technique 
        [3, 3, 1]
         l  r
         
         1. Start with l and r pointers
         2. while l < r
                calculate the volume and update max
                Always move the pointer with the smaller line towards the other end
         3. return max
        
        [6, 2, 5, 4]
         l  r
         
         max = 12
         (2-0)*5 = 10
         
            Is there a scenario where we want to move the pointer with the taller line?
            
            If you move the taller line you have a chance to increase the volume 
        """
        l, r = 0, len(height)-1
        res = 0
        while l < r:
            cur = (r-l) * min(height[r], height[l])
            res = max(res, cur)
            if height[r] > height[l]:
                l+=1
            else:
                r-=1
        return res