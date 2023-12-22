class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        h = 8
        
        k = 4

        Brute force:
        Starting at min iterating to max, 
            find total cost

        Want minimum number where h is satisfied,
        m is not satisfied
        m + 1 is satisfied
        """

        def satisfied(k):
            hours = 0
            for i, p in enumerate(piles):
                hours += p // k
                minutes = p % k

                if minutes:
                    hours += 1
            if hours <= h:
                return True
            return False

        maximum = max(piles)

        i, j = 1, maximum + 1
        while i <= j:
            m = (i+j)//2
            isSatisfied = satisfied(m)
            if not isSatisfied:
                if satisfied(m+1):
                    return m+1
                i = m + 1
            elif isSatisfied:
                if m == 1:
                    return m
                j = m - 1
        return -1