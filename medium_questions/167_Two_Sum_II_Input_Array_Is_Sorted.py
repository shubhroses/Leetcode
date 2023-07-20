class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        l, r = 0, len(numbers)
        while l<r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            else if numbers[l] + numbers[r] < target:
                l += 1
            else if numbers[l] + numbers[r] > target:
                r -= 1
        
        """
        l, r = 0, len(numbers)-1
        while l<r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
        """
        numbers = [2, 5, 7]
                      l  r
        target = 12

last element of a array is len(arr)-1
its elif in python
Explain why you are doing what you are doing
        """