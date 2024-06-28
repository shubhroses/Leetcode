class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquares(num):
            res = 0
            for d in str(num):
                res += int(d)**2
            return res
        
        slow, fast = n, n

        while slow != 1 and fast != 1:
            slow = sumSquares(slow)
            fast = sumSquares(fast)
            fast = sumSquares(fast)

            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False
        return True
        
        
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = sum([int(d)**2 for d in str(n)])
        if n == 1:
            return True
        return False


class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        def helper(numbr):
            if numbr in visited:
                return False
            if numbr == 1:
                return True
            visited.add(numbr)
            newNum = sum(int(c)**2 for c in str(numbr))
            return helper(newNum)

        return helper(n)
