class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        l, r as pointers in each string
        if the chars are equal: can increment both or just l
        if reach end of both strings return 1
        if reach end of s but not t return 0
        if reach end of t but not s reaturn 0
        if the chars are not equal return 0
        """
        memo = {}
        def helper(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if r == len(t):
                return 1
            if l == len(s):
                return 0

            count = 0
            if s[l] == t[r]:
                count = helper(l + 1, r + 1) + helper(l + 1, r)
            else:
                count = helper(l + 1, r)

            memo[(l, r)] = count
            return memo[(l, r)]

        return helper(0, 0)
