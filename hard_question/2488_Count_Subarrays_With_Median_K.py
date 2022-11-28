class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Find the index of k in nums
        index = nums.index(k)
        
        # l (larger) is count of element>k
        # s (smaller) is count of element<k
        res = l1 = s1 = 0
        before = defaultdict(int)
        
        # run from index-1 to 0 (before index)
        for i in reversed(range(index)):
            # Increase l or s, and increase the differece in 'before'
            if nums[i] > k: l1 += 1
            else: s1 += 1
            before[(l1-s1)] += 1
            
            # If the number of larger element and smaller element are the same,
            # we find a valid subarray which is nums[i:index+1], so increase res.
            if l1-s1==1 or l1-s1==0: res += 1

        l2 = s2 = 0
        for i in range(index+1,len(nums)):
            if nums[i] > k: l2 += 1
            else: s2 += 1
            
            # we need the number of larger elements and smaller elements to be the same in a subarray,
            #    l1 + l2 == s1 + s2 or l1 + l2 + 1 == s1 + s2
            # => l1 - s1 == s2 - l2 or l1 - s1 == s2 - l2 + 1
            # so we need to check if s2-l2 or s2-l2+1 exist in before
            res += before[s2-l2] + before[s2-l2+1]
            
            if l2-s2==1 or l2-s2==0: res += 1
                
        return res+1