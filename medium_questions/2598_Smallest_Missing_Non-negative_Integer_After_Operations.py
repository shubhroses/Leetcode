class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        """
        Create a counter from nums such that {0: count, 1: count}
        {rem: count}, remainder 0 to value is a count
        
        then find the min value and if there are multiple min values find min key with that value, lets say 5:3, and value is 7, the number is 7*3 = 21 + 5-1 = 25
        1234567
        1234567
        1234567
        1234567
        """
        remCount = {i:0 for i in range(value)}
        for num in nums: 
            rem = num % value
            remCount[rem] += 1
            
        # print(remCount)
        
        mn = min(remCount.values())
        
        # print(mn) 
        
        small = 0 
        for i in range(value):
            small = i
            if remCount[i] == mn:
                break
        # print(small)
        
        tot = value*mn + small
        return tot
    