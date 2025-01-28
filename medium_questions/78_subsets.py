class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        at each index, can either take or leave
        """
        subsets = []
        subsets.append([])
        for currentNumber in nums:
            n = len(subsets)
            for i in range(n):
                set = list(subsets[i])
                set.append(currentNumber)
                subsets.append(set)
        return subsets

"""
Create a res []
add empty list to res

for each number in nums
get length of res
for each element in res, add a duplicate with an appended new element
"""

        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
