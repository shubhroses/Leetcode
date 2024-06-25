class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join([str(n) for n in digits]))
        num += 1
        res = [int(c) for c in str(num)]
        return res


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        increment the last number, if last number is 9 set to 0
        if last number is 0, need to increment number ot left


        9

        0
        i
        prevZero = True
        """
        reversed = digits[::-1]
        prevZero = True
        i = 0
        while i < len(digits) and prevZero:
            reversed[i] = (reversed[i] + 1) % 10
            if reversed[i] != 0:
                prevZero = False
            i += 1
        if prevZero:
            reversed.append(1)
        return reversed[::-1]


        

        
