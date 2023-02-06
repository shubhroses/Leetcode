class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        find longest substrings with 1 distinct character

        abcabcbb
               l
               r

        visited = {a, b, c}

        res = 3

        """
        visited = set()

        l = 0
        res = 0
        for r, c in enumerate(s):
            while c in visited:
                visited.remove(s[l])
                l+=1
            visited.add(c)
            res = max(res, r-l+1)
        return res