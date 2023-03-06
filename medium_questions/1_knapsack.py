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

if __name__ == "__main__":
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))