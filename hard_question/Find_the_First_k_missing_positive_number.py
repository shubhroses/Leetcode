def find_first_k_missing_positive(nums, k):
    n = len(nums)
    i = 0
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    missingNumbers = []
    extraNumbers = set()

    for i in range(n):
        if len(missingNumber) < k:
            if nums[i] != i + 1:
                missingNumbers.append(i + 1)
                extraNumbers.add(nums[i])
    
    i = 1
    while len(missingNumbers) < k:
        candidateNumber = i + n
        if candidateNumber not in extraNumbers:
            missingNumbers.append(candidateNumber)
        i += 1
    
    return missingNumbers