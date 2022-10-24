class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        select candidates until teach target
        Can choose same number again

        candidates = [1, 3, 5, 7]
                         i
        target = 5
        
        ind = 0
        selected = [1, 1, 3]
        total = 0
        
        """
        if not candidates or not target:
            return []
        res = []
        def helper(ind, selected, total):
            if total > target:
                return 
            if total == target:
                res.append(selected)
                
            for i in range(ind, len(candidates)):
                helper(i, selected + [candidates[i]], total + candidates[i])
        
        helper(0, [], 0)
        return res
            
        