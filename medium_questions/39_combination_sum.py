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
            
        class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Sort candidates

        if cur creater than target: stop

        if cur = target:
            add to res
        
        at each index can take or leave
        """

        res = []
        candidates.sort()

        def helper(i, cur, curSum):
            if curSum == target:
                res.append(cur.copy())
                return

            if i == len(candidates) or curSum > target:
                return
            
            # take stay
            cur.append(candidates[i])

            helper(i, cur, curSum + cand idates[i])

            cur.pop()

            # leave
            helper(i+1, cur, curSum)

        helper(0, [], 0)

        return res


