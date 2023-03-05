def solve_knapsack(profits, weights, capacity):
    def knapsack_recursive(cap, current_index):
        if cap <= 0 or current_index >= len(profits):
            return 0

        profit1 = 0
        if weights[current_index] <= cap:
            profit1 = profits[current_index] + knapsack_recursive(cap - weights[current_index], current_index + 1)
        
        profit2 = knapsack_recursive(cap, current_index + 1)
        return max(profit1, profit2)

    return knapsack_recursive(capacity, 0)

if __name__ == "__main__":
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))