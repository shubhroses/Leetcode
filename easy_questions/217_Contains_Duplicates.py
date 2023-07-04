class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elements = set()
        for i, e in enumerate(nums):
            if e in elements:
                return True
            elements.add(e)
        return False