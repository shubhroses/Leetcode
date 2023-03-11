nums = [3, 34, 4, 12, 5, 2]
k = 9

def isSubsetSum(i, curSum):
    if curSum == k:
        return True
    if i >= len(nums):
        return False
    
    # Take
    take = isSubsetSum(i+1, curSum + nums[i])

    # Leave
    leave = isSubsetSum(i+1, curSum)

    return take or leave
    
 
 
# Driver code

if (isSubsetSum(0, 0) == True):
    print("Found a subset with given k")
else:
    print("No subset with given k")