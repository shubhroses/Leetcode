class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        for i in range(len(nums)-k+1):
            cur = nums[i]
            notConsec = False
            for j in range(i+1, i+k):
                if nums[j] - cur != 1:
                    notConsec = True
                    break
                cur = nums[j]
            if notConsec:
                res.append(-1)
            else:
                res.append(cur)
        return res

        

        # 3254_Find_the_Power_of_K-Size_Subarrays_I.py
