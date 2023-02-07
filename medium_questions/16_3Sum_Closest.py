class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float("inf")
        diff = float("inf")

        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if abs(target - threeSum) < diff:
                    res = threeSum
                    diff = abs(target - threeSum)
                if threeSum > target:
                    r-=1
                elif threeSum < target:
                    l+=1
                else:
                    break
        
        return res