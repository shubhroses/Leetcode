#
#
#
"""
When using a 2d array for memoization, have to do this method
[[-1 for x in range(capacity+1)] for y in range(len(profits))]
Where y is the number of rows and y is the number of cols
So when accessing

memo[row][col]
"""
def solve_knapsack_memo(profits, weights, capacity):
    memo = [[-1 for x in range(len(weights))] for y in range(capacity + 1)]
    def helper(currentCapacity, ind):
        if currentCapacity <= 0 or ind >= len(profits):
            return 0
        if memo[currentCapacity][ind] != -1:
            return memo[currentCapacity][ind]

        # Take
        take = 0
        if weights[ind] <= currentCapacity:
            take = helper(currentCapacity - weights[ind], ind + 1) + profits[ind]
        leave = helper(currentCapacity, ind + 1)

        memo[currentCapacity][ind] = max(take, leave)
        return memo[currentCapacity][ind]
    
    return helper(capacity, 0)


def solve_knapsack_bottom_up(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    
    dp = [[0 for x in range(capacity + 1)] for y in range(n)]

    # Every thing with capacity 0 has max profit set to 0
    for i in range(0, n):
        dp[i][0] = 0
    
    # For the 0th index, if the capacity is greater than weight than change max profit to the profit at that index
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]


    # For each index
    for i in range(1, n):

        # For each capacity
        for c in range(1, capacity+1):


            profit1, profit2 = 0, 0

            # if the weight at that index is less than the capacity
            if weights[i] <= c:
                # Take
                profit1 = profits[i] + dp[i-1][c-weights[i]]
            
            # Leave
            profit2 = dp[i-1][c]

            dp[i][c] = max(profit1, profit2)
    return dp[n-1][capacity]

def solve_knapsack_recursive(profits, weights, capacity):
    """
    Base case:
        Make sure that currenty capacity is > 0 and the current index is less than the length of the arrays

    Take:
        helper(currentCapacity - weights[ind], ind + 1) + profits[ind]

    Leave:
        helper(currentCapacity, ind + 1)

    return max(take, leave)
    """
    def helper(currentCapacity, ind):
        if currentCapacity <= 0 or ind >= len(profits):
            return 0

        # Take
        
        take = 0
        if weights[ind] <= currentCapacity:
            take = helper(currentCapacity - weights[ind], ind + 1) + profits[ind]
        leave = helper(currentCapacity, ind + 1)

        return max(take, leave)
    return helper(capacity, 0)

if __name__ == "__main__":
    print(solve_knapsack_memo([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack_memo([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack_memo([1, 6, 10, 16], [1, 2, 3, 5], 7))#
#
