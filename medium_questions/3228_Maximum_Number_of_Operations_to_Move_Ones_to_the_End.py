class Solution:
    def maxOperations(self, s: str) -> int:
        """
        From 1001101
        create : (1,1), (0, 2), (1, 2), (0, 1), (1, 1)
        """
        # s = "3228. Maximum Number of Operations to Move Ones to the End"
        # print('_'.join(s.replace('.', '', 1).split()) + ".py")
        saved = []
        for i, c in enumerate(s):
            if saved and c == saved[-1][0]:
                saved[-1][1] += 1
            else:
                saved.append([c, 1])
        # print(saved)
        zeroCount = 0
        res = 0
        for i in range(len(saved)-1, -1, -1):
            b, c = saved[i]

            if b == '1':
                res += (zeroCount * c)
            else:
                zeroCount += 1
        return res
        

        
