def find_corrupt_numbers(nums):
    # i = 0
    # while i < len(nums):
    #     j = nums[i]-1
    #     if nums[i] != nums[j]:
    #         nums[i], nums[j] = nums[j], nums[i]
    #     else:
    #         i += 1
    i = 0
    while i < len(nums):
        j = nums[i]-1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i, n in enumerate(nums):
        if i+1 != n:
            return [n, i+1]
    return [-1, -1]
    


print(find_corrupt_numbers([3, 1, 2, 5, 2]))
print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))


"""
[ 1, 2, 3, 2, 5]
  0  1  2  3  4

[2, 4]
"""