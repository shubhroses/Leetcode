class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        """
        Write a method to determine is special

        Create a set of all proper divisors


        1: 1
        2: 1, 2
        3: 1, 3
        4: 1, 2, 4
        5: 1, 5
        6: 1, 2, 3, 6
        7: 1, 7
        8: 1, 2, 4, 8
        9: 1, 3, 9
        10: 1, 2, 5, 10

        create a set of special numbers
        iterate through all prime numbers and add their p**2 to special


        find all prime numbers between 0-r+1

        """ 
        num = int(math.sqrt(r))
        special = 0
        while num * num >= l and num * num <= r:
            flag = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    flag = False
                    break
            if flag:
                special += 1
            num -= 1

        ans = r - l + 1 - special
        if l == 1:
            ans += 1
        return ans