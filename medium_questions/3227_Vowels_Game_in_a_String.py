class Solution:
    def doesAliceWin(self, s: str) -> bool:

        # s = "3227. Vowels Game in a String"
        # print('_'.join(s.replace('.', '', 1).split()) + ".py")
        bits = []
        for c in s:
            if c in ['a', 'e', 'i', 'o', 'u']:
                bits.append(1)
            else:
                bits.append(0)

        memo = {}
        def helper(turn, i, vCount):
            if (turn, i, vCount) in memo:
                return memo[(turn, i, vCount)]
            if i == len(bits):
                if turn == 'A':
                    return False
                else:
                    return True

            if bits[i] == 1:
                vCount += 1

            take = leave = None
            if turn == 'A':
                if vCount % 2 == 1: # Can take
                    take = helper('B', i + 1, vCount)
                    leave = helper('A', i + 1, vCount)
                else: # cant take
                    leave = helper('A', i + 1, vCount)

            elif turn == 'B':
                if vCount % 2 == 1: # Cant take
                    take = helper('B', i + 1, vCount)
                else: #can take
                    take = helper('B', i + 1, vCount)
                    leave = helper('A', i + 1, vCount)
            memo[(turn, i, vCount)] = take or leave
            return memo[(turn, i, vCount)]
            
        return helper('A', 0, 0)
