class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(cost):
                return 0
            oneStep = dfs(i+1) + cost[i]
            twoStep = dfs(i+2) + cost[i]
            memo[i] = min(oneStep, twoStep)
            return memo[i]

        return min(dfs(0), dfs(1))

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = [float("inf") for _ in range(len(cost))]

        memo[0], memo[1] = cost[0], cost[1]

        for i in range(2, len(memo)):
            memo[i] = min(memo[i-1], memo[i-2]) + cost[i]
        
        return min(memo[-1], memo[-2])
