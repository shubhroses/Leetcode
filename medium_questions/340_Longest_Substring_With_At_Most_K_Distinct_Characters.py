class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        Sliding window with counter

        "eceba"
            l
             r

        k = 2

        counter = {b:1, a:1}
        res = 3

        """
        l = 0
        counter = {}
        res = float("-inf")
        for r, c in enumerate(s):
            counter[c] = counter.get(c, 0) + 1

            while len(counter) > k:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l+=1
            res = max(res, r-l+1)
        return res