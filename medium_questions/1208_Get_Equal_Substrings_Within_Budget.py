class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        Want to change s to t

        Create str called distance

        

        What is the largest substring in cost string that we cna fford with maxCost
        """
        costArr = [abs(ord(s[i])-ord(t[i])) for i in range(len(s))]
        res = 0
        curPrice = 0
        l = 0

        for r in range(len(s)):
            curPrice = costArr[r] + curPrice
            if curPrice <= maxCost:
                res = max(res, r-l+1)
            while curPrice > maxCost:
                curPrice -= costArr[l]
                l+=1
        return res
        """
        abcd
        bcdf
        1112
          l
           r

        maxCost = 3
        res = 3
        curPrice = 2
        """