class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        A = [i for i,c in enumerate(s) if c == '|']
        res = []
        for a,b in queries:
            i = bisect.bisect_left(A, a)
            j = bisect.bisect(A, b) - 1
            res.append((A[j] - A[i]) - (j - i) if i < j else 0)
        return res


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
            0123456789
            **|**|***|
        
plateCount  1223445677

candleLeft -1-122255559

candleRight 2225559999

[2, 5]

candleRight[2] = 2
candleLeft[5] = 5

plateCount[candleLeft[5]] - plateCount[candleRight[2]] =>
plateCount[5] - plateCount[2] =>
4 - 2 = 2
        
        """
        plateCount = []
        candleLeft = []
        candleRight = []
        
        p = 0
        b = -1
        for i, c in enumerate(s):
            if c == "*":
                p += 1
            plateCount.append(p) 
            
            if c == "|":
                b = i
            candleLeft.append(b)
        
        b = -1
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            if c == "|":
                b = i
            candleRight.append(b)
        candleRight = candleRight[::-1]
        print(plateCount)
        print(candleLeft)
        print(candleRight)
        
        
        res = []
        for l, r in queries:
            if candleLeft[r] < l or candleRight[l] > r:
                res.append(0)
            else:
                res.append(plateCount[candleLeft[r]] - plateCount[candleRight[l]])
        return res
    
        """
            0123456
            ***|**|
candleCount 1233455
candleLeft  ---3336
candleRight 3333666

l = 4
r = 5
candleRight[l] = 6
candleLeft[r] = 3


        """