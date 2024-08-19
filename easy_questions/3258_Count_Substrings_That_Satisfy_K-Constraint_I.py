class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        """
        count 0's < k
        count 1's < k

        brute force look at every substring
        maintain counter
        """
        res = 0
        for l in range(len(s)):
            for r in range(l+1, len(s)+1):
                oneCount = 0
                zeroCount = 0
                substr = s[l:r]
                for c in substr:
                    if c == '1':
                        oneCount += 1
                    elif c == '0':
                        zeroCount += 1
                
                if oneCount <= k or zeroCount <= k:
                    res += 1
        return res

        # 3258_Count_Substrings_That_Satisfy_K-Constraint_I.py
