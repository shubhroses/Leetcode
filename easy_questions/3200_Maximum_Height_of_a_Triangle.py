class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        """
        1, 2, 3, 4, 5, 6, 7, 8

        maxHeight 
        One color: will be all odd numbers in range [1, maxHeight]
        Other color: will be all even numbers in range [1, maxHeight]

        Need formula for finding sum of all numbers between 0 and maxHeight


        3
        odd = 1 + 3 = 4
        even = 2

        4
        odd = 1 + 3
        even = 2 + 4

        curNum = 0

    

        redLeft = 0
        blueLeft = 0

        res = 2
        i = 4
        """
        redLeft, blueLeft = red, blue
        res = 0
        i = 1
        while True:
            if i % 2 == 1: # ODD
                if redLeft >= i:
                    redLeft -= i
                else:
                    break
            else: # EVEN
                if blueLeft >= i:
                    blueLeft -= i
                else:
                    break
            i += 1
        res = max(res, i-1)
        
        redLeft, blueLeft = red, blue
        i = 1
        while True:
            if i % 2 == 0: # EVEN
                if redLeft >= i:
                    redLeft -= i
                else:
                    break
            else: # ODD
                if blueLeft >= i:
                    blueLeft -= i
                else:
                    break
            i += 1
        res = max(res, i-1)
        return res
