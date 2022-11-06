class Solution:
    def minSwaps(self, s: str) -> int:
        def countSwaps(start):
            cntWrongPos = 0
            for c in s:
                if start != c:
                    cntWrongPos += 1
                start = '1' if start == '0' else '0'
            return cntWrongPos // 2

        cntOne = s.count('1')
        cntZero = len(s) - cntOne
        if abs(cntOne - cntZero) > 1: # Invalid
            return -1
        if cntZero > cntOne:  # zero must be on even position
            return countSwaps('0')
        if cntZero < cntOne:  # One must be on even position
            return countSwaps('1')
        return min(countSwaps('0'), countSwaps('1'))  # get min swaps between 2 case (zero start first or one start first)