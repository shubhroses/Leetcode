
def minimumDifference(nums):
    s = sum(nums)
    dp = [[-1 for x in range(s+1)] for y in range(len(nums))]

    def helper(i, s1, s2):
        if i == len(nums):
            return abs(s1 - s2)
        
        if dp[i][s1] == -1:
            dif1 = helper(i+1, s1 + nums[i], s2)
            dif2 = helper(i+1, s1, s2 + nums[i])
            dp[i][s1] = min(dif1, dif2)
        
        return dp[i][s1]

    return helper(0, 0, 0)

def minimumDifferenceDP(nums):
    s = sum(nums)
    n = len(nums)
    dp = [[False for x in range(int(s/2)+1)] for y in range(n)]

    for i in range(0, n):
        dp[i][0] = True

    for j in range(0, int(s/2)+1):
        dp[0][j] = nums[0] == j

    for i in range(1, n):
        for j in range(1, int(s/2) + 1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i-1][j-nums[i]]
            
    sum1 = 0

    for i in range(int(s/2), -1, -1):
        if dp[n-1][i]:
            sum1 = i
            break
    sum2 = s - sum1
    return abs(sum2-sum1)


if __name__ == "__main__":
    print(minimumDifferenceDP([1, 2, 3, 9]))
    print(minimumDifferenceDP([1, 2, 7, 1, 5]))
    print(minimumDifferenceDP([1, 3, 100, 4]))