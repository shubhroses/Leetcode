class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        counter = {}
        for ind, count in nums1:
            counter[ind] = counter.get(ind, 0) + count
        for ind, count in nums2:
            counter[ind] = counter.get(ind, 0) + count
        res = []
        for ind in sorted(counter.keys()):
            res.append([ind, counter[ind]])
        return res