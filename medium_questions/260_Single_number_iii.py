class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        XOR properties 
        1^0 = 1
        32^32 = 0
        32^0 = 32

        cur number will be num1^num2
        """
        n1xn2 = 0
        for n in nums:
            n1xn2^= n
        
        rightmost_set_bit = 1
        while (rightmost_set_bit & n1xn2) == 0:
            rightmost_set_bit = rightmost_set_bit << 1
        
        num1, num2 = 0, 0

        for num in nums:
            if (num & rightmost_set_bit) != 0:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]