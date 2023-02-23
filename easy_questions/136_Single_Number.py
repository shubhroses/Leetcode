class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        XOR properties

        1^0 = 1
        32^32 = 0
        32^0 = 32

        Just xor every number in nums together, the duplicates will cancel out leaving single number
        """
        cur = 0
        for n in nums:
            cur = cur^n
        return cur