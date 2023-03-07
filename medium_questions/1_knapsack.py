def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    def knapsack_recursive(cap, current_index):
        if cap <= 0 or current_index >= len(profits):
            return 0
        
        if dp[current_index][cap] != -1:
            return dp[current_index][cap]

        profit1 = 0

        # Take
        if weights[current_index] <= cap:
            profit1 = profits[current_index] + knapsack_recursive(cap - weights[current_index], current_index + 1)
        
        # Leave
        profit2 = knapsack_recursive(cap, current_index + 1)

        dp[current_index][cap] = max(profit1, profit2)
        return dp[current_index][cap] 

    return knapsack_recursive(capacity, 0)

def solve_knapsack_bottom_up(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    
    dp = [[0 for x in range(capacity + 1)] for y in range(n)]

    for i in range(0, n):
        dp[i][0] = 0
    
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0

            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]
            
            profit2 = dp[i-1][c]

            dp[i][c] = max(profit1, profit2)
    return dp[n-1][capacity]

if __name__ == "__main__":
    print(solve_knapsack_bottom_up([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack_bottom_up([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack_bottom_up([1, 6, 10, 16], [1, 2, 3, 5], 7))