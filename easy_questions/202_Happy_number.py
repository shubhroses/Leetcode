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