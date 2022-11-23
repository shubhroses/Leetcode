def isSubsetSum(arr):
    if sum(arr) % 3 !=  0:
        return False

    third = sum(arr)//3
    n = len(arr)
    
    subset =([[False for i in range(third + 1)] for i in range(n + 1)])
      
    for i in range(n + 1):
        subset[i][0] = True

          
    for i in range(1, third + 1):
        subset[0][i]= False

              
    # Fill the subset table in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, third + 1):
            if j < arr[i-1]:
                subset[i][j] = subset[i-1][j]
            if j >= arr[i-1]:
                subset[i][j] = (subset[i-1][j] or subset[i - 1][j-arr[i-1]])

    for row in subset:
        print(row)
      
    # uncomment this code to print table 
    # for i in range(n + 1):
    #     for j in range(third + 1):
    #         print (subset[i][j], end =" ")
    #     print()
    return subset[n][third]

arr = [3, 4, 2, 5, 7]
 
# Function call
if (isSubsetSum(arr) == True):
    print("Found a subset with given third")
else:
    print("No subset with given third")