class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """
        Brute force:
            4 for loops that check each tuple to see if it sums to zero 
            
        1. Create counter of all sums in A, B
        2. Iterate through all tuples in C,D and see if complement in counter
        3. Add to count
        """
        
        num_dict = {}
        for a in A:
            for b in B:
                s = a + b
                num_dict[s] = num_dict.get(s, 0) + 1
        count = 0
        for c in C:
            for d in D:
                inverse = 0 - (c + d)
                count += num_dict.get(inverse, 0)
        return count