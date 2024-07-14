class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        res = 0

        ump = collections.defaultdict(int)

        for h in hours:
            res += ump[(24 - h%24)%24]
            ump[h%24] += 1
        return res

        

