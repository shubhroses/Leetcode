def pair_with_targetsum(arr, target_sum):
    i, j = 0, len(arr)-1

    while i < j:
        if arr[i] + arr[j] < target_sum:
            i+=1
        elif arr[i] + arr[j] > target_sum:
            j-=1
        else:
            return [i,j]

    return [-1,-1]

print(pair_with_targetsum(arr=[1,2,3,4,6], target_sum=6))
print(pair_with_targetsum(arr=[2,5,9,11], target_sum=11))