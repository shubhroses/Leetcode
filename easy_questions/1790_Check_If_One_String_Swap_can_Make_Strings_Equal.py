class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        num = 0
        saved = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                saved.append([s1[i], s2[i]])
                num += 1
        if num == 2:
            if len(saved) == 2 and saved[0][0] == saved[1][1] and saved[0][1] == saved[1][0]:
                return True
        if num == 0:
            return True
        return False 