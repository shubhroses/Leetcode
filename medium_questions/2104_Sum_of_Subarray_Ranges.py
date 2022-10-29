class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        Find every sub array 
        Take the max and min, return range
        
        [1, 3, 2, 5]
        
        2 + 1 + 3 + 2 + 3 + 4 = 15
        
        [0, 2, 2, 4]
        
        [4  3  3  0]

        """
        def fn(op): 
            """Return min sum (if given gt) or max sum (if given lt)."""
            ans = 0 
            stack = []
            for i in range(len(nums) + 1): 
                while stack and (i == len(nums) or op(nums[stack[-1]], nums[i])): 
                    mid = stack.pop()
                    ii = stack[-1] if stack else -1 
                    ans += nums[mid] * (i - mid) * (mid - ii)
                stack.append(i)
            return ans 
        
        return fn(lt) - fn(gt)