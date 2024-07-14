class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        """
        Keep a count of hCuts and vCuts

        order list (cost, dir) from max to min

        iterate through list

        if dir = horizontal:
            res += vCuts + 1 * cost

        """
        res = 0

        cuts = []
        for h in horizontalCut:
            cuts.append((h, 'h'))
        for v in verticalCut:
            cuts.append((v, 'v'))
        
        cuts.sort(key = lambda x:x[0], reverse=True)

        vCuts, hCuts = 1, 1
        for cost, dir in cuts:
            if dir == 'h':
                res += vCuts * cost
                hCuts += 1
            else:
                res += hCuts * cost
                vCuts += 1
        return res

        # 100361_minimum_cost_for_cutting_cake_1.py
