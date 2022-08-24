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