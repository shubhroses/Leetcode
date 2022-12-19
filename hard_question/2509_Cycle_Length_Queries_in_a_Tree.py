class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        def getLen(x, y):
            
            xPath = 0
            yPath = 0
            while x > 1 or y > 1:
                if x > y:
                    x = x//2
                    xPath += 1
                elif y > x:
                    y = y//2
                    yPath += 1
                else:
                    break
            return xPath + yPath + 1
        
        res = []
        for l, r in queries:
            res.append(getLen(l, r))
            
        return res