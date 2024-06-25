class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join([str(n) for n in digits]))
        num += 1
        res = [int(c) for c in str(num)]
        return res

        
