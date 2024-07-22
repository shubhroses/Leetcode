class Solution:
    def losingPlayer(self, s:int, y:int) -> str:
        if min(x, y//4)%2==1:
            return "Alice"
        else:
            return "Bob