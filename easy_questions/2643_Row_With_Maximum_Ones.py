class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        sArr = []
        for arr in mat:
            sArr.append(sum(arr))
        mx = max(sArr)
        return [sArr.index(mx), mx]
    