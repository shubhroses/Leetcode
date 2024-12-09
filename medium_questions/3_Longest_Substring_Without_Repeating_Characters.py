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
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Maintain a left a right pointer
        a map of all elements and position in window
        If the right pointer encounters a duplicate elements
        move the left pointer until reach index of previos elements
        Maintain a result array

        012345
        pwwkew
              l
             r

        window = {w, k, e}
        res = 3
        """
        l = 0
        window = set()
        res = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, r-l+1)
        return res




        
