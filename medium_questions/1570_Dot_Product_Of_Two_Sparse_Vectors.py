class SparseVector:
    def __init__(self, nums: List[int]):
        """
        [1, 0, 0, 2, 3]
         0. 1. 2. 3. 4
         
        saved = {0:1, 3:2, 4:3}
        # Counter index:value, where value is not 0
        
        saved.get(1, 0) = 0
        
        saved1 = {0:1, 3:2, 4:3}
        saved2 = {1:3, 3:4}
        
        res = 0
        for key in saved1.keys:
            res += saved1[key] * saved2.get(key, 0)
        
        """ 
        self.saved1 = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.saved1[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        saved2 = vec.saved1
        res = 0
        for key in self.saved1.keys():
            res += self.saved1[key] * saved2.get(key, 0)
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)