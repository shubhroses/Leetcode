class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}
        for i, e in enumerate(nums):
            if target-e in elements:
                return [i, elements[target-e]]
            elements[e] = i