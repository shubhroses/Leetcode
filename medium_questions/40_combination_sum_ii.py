class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()

        def helper(i, cur, s):
            if s == target:
                self.res.append(cur)
                return
            if i == len(candidates) or s > target:
                return
            # take
            helper(i+1, cur + [candidates[i]], s + candidates[i])
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            # leave
            helper(i+1, cur, s)
        
        helper(0, [], 0)
        return self.res