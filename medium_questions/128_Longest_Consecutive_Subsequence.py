class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Add all elements to a set
        if n-1 in set 
        """
        s = set(nums)
        mx = float("-inf")
        for n in nums:
            if n-1 not in s:
                c = 0
                n1 = n
                while n1 in s:
                    c+=1
                    n1+=1
                mx = max(mx, c)
        if mx == float("-inf"):
            return 0
        return mx
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        1. Add all elements in nums into a set
        2. Find starting elements: For each element where element - 1 is not in the set
        3. Start counting up by one and stop until new element not in set
        4. Return max count

        1. Create set from nums s
        2. starting = []
        3. For num in s: 
            if num-1 not in s:
                starting.append(num)
        4. res = 0
        5. For num in starting:
            count = 1
            while num+1 in s:
                count += 1
                num = num + 1
            res = max(res, count)
        6. Return res

        s = [100, 4, 200, 1, 3, 2]
        starting = [100, 200, 1]
        res = 4
        num = 1
            count = 4
        return res
        """
        s = set(nums)
        starting = []
        for num in s:
            if num-1 not in s:
                starting.append(num)
        res = 0
        for num in starting:
            count = 1
            while num+1 in s:
                count += 1
                num = num + 1
            res = max(res, count)
        return res