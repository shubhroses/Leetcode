class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        """
        Get a difference array 

        """
        # s = "3229. Minimum Operations to Make Array Equal to Target"
        # print('_'.join(s.replace('.', '', 1).split()) + ".py")

        res = pre = 0

        diff = []
        for i in range(len(nums)):
            diff.append(target[i] - nums[i])

        for i in range(len(nums)):
            res += max(diff[i] - pre, 0)
            pre = diff[i]
        
        return res + max(-1 * pre, 0)

