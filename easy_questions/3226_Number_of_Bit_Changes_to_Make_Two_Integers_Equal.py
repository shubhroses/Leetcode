class Solution:
    def minChanges(self, n: int, k: int) -> int:
        """
        1101
        0100
           i
        """
        # s = "3226. Number of Bit Changes to Make Two Integers Equal"
        # print('_'.join(s.replace('.', '', 1).split()) + ".py")
        one_count = 0
        while n:
            if n % 2 == 0 and k % 2 == 1:
                return -1
            elif n % 2 == 1 and k % 2 == 0:
                one_count += 1
            n = n >> 1
            k = k >> 1

        if k:
            return -1
        return one_count
