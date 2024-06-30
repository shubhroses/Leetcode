class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        """

        [1,2,1,1,2,1,2]

        [3,3,2,3,3,3]
        6

        [1,2,1,2,2,1,2]
        [3,3,3,4,3,3]
        6

        Iterate through, sum pairs, count even and odd


        [1,8,4,2,4]
         l       r

        firstEven = 1
        firstOdd = 0

        evenRes1 = 3
        oddRes1 = 0

        evenRes2 = 0
        oddRes2 = 1

        """

        firstEven = firstOdd = len(nums)
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                firstEven = i
                break
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                firstOdd = i
                break

        evenRes1 = oddRes1 = 0
        l = firstEven
        for r in range(l+1, len(nums)):
            if (nums[l] + nums[r]) % 2 == 1:
                oddRes1 += 1
                l = r
        
        l = firstEven
        for r in range(l+1, len(nums)):
            if (nums[l] + nums[r]) % 2 == 0:
                evenRes1 += 1
                l = r

        evenRes2 = oddRes2 = 0
        l = firstOdd
        for r in range(l+1, len(nums)):
            if (nums[l] + nums[r]) % 2 == 1:
                oddRes2 += 1
                l = r
        
        l = firstOdd
        for r in range(l+1, len(nums)):
            if (nums[l] + nums[r]) % 2 == 0:
                evenRes2 += 1
                l = r

        return max(oddRes1, evenRes1, oddRes2, evenRes2) + 1
        
