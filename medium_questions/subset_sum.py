nums = [3, 34, 4, 12, 5, 2]
k = 9

dp = [[False for x in range(k+1)] for y in range(len(nums))]

def isSubsetSum(i, sum):
    n = len(nums)

    for i in range(0, n):
        dp[i][0] = True

    for s in range(1, sum+1):
        dp[0][s] = True if nums[0] == s else False

    for i in range(1, n):
        for s in range(1, sum+1):
            if dp[i-1][s]:
                dp[i][s] = dp[i-1][s]
            elif s >= nums[i]:
                dp[i][s] = dp[i-1][s-nums[i]]
    return dp[n-1][sum]
    
 
 
# Driver code

if (isSubsetSum(0, 0) == True):
    print("Found a subset with given k")
else:
    print("No subset with given k")