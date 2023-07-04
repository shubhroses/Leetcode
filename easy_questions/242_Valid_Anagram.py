class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sC = Counter(s)
        tC = Counter(t)
        if sC == tC:
            return True
        return False