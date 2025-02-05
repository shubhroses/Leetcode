class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        res.append([])
        startIndex, endIndex = 0, 0
        for i in range(len(nums)):
            startIndex = 0
            if i > 0 and nums[i] == nums[i-1]:
                startIndex = endIndex + 1
            endIndex = len(res)-1

            for j in range(startIndex, endIndex + 1):
                temp = list(res[j])
                temp.append(nums[i])
                res.append(temp)
        return res
    

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """

        """
        self.res = []
        nums.sort()
        def helper(i, cur):
            if i == len(nums):
                self.res.append(cur)
                return
            
            #Take
            helper(i+1, cur + [nums[i]])
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            #Leave
            helper(i+1, cur)
        
        helper(0, [])

        return self.res


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        A teach index can take or leave
        """
        res = set()

        def backtrack(i, subset):
            if i == len(nums):
                res.add(tuple(subset))
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            backtrack(i + 1, subset)

        nums.sort()
        backtrack(0, [])
        return [list(s) for s in res]

