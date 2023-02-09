class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        For overlapping intervals take max of start and min of end
        """
        i, j = 0, 0
        res = []

        while i < len(firstList) and j < len(secondList):
            sA, eA = firstList[i]
            sB, eB = secondList[j]

            if eA < sB:
                i += 1
            elif eB < sA:
                j += 1
            else:
                res.append([max(sA, sB), min(eA, eB)])
                if eA < eB:
                    i += 1
                else:
                    j += 1
        return res