class Solution:
    def minimumLength(self, s: str) -> int:
        """
        If there is an odd count of a character it can go down to 1
        if there is an even count it can go down to 2
        """
        counter = collections.defaultdict(int)
        for c in s:
            counter[c] += 1
        
        res = 0
        for char, count in counter.items():
            if count % 2 == 1:
                res += 1
            else:
                res += 2
        return res