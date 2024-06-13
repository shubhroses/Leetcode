class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charToPos = {}
        for i, c in enumerate(s):
            charToPos[c] = i
        res = []
        l, last = 0, 0
        for r in range(len(s)):
            last = max(last, charToPos[s[r]])
            if last == r:
                res.append(r-l+1)
                l = r+1
        return res

