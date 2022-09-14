class Solution:
    def largestVariance(self, s: str) -> int:
        """
        For each substring, calculate variance and return max
        
        n^2, then create counter of each substring and do max counter - min counter
        maintain global counter to avoid creating one each time, getting max and min log(n)
        logn*n^2
        
        s = "aabbb"
             l
                 r
        
        c = {a: 2,
             b: 1 }
        cur = ""
        remaining = "aab"
        
        1. For each pair of letters iterate through string
        2. Maintain frequency of each character
        3. If frequency of c2 > frequency of c1 reset f1 and f2 = 0
        
        """
        """
        "a  a  b"
         c1 c2 
        
        for every c1 and c2 in alphabet: 
            iterate through s:
                a. b. c. d. e. f. g  
        freq = [2, 1, 0, 0, 0, 0, 0]
        
        maxVar = 0
        c1 = a
        c2 = b
        
        if same letter skip, if either zero skip
        
        "e  f  f"
            c
        
        freq = [0, 0, 1, 2]
        
        maxVar = 0
        a = 3 == 'e'
        b = 4 == 'f'
        
        curAFreq = 1
        curBFreq = 2
        
        remainingA = 0
        remainingB = 2
        
        
        
        """
        res = 0
        chars = list(set(s))
		
		# Loop through each pari of (c1, c2)
        for i in range(len(chars)):
            for j in range(i+1, len(chars)):
                c1, c2 = chars[i], chars[j]
				
				# keep track of count(c1) - count(c2) 
                diff = 0 
				
				# max and min of diff
				# result should be maximum of (diff - min_diff, max_diff - diff)
				# e.g. "baabaa", at index = 0, min_diff = -1. when index = 5, diff = 4 - 2 = 2, result = diff - min_diff = 2 - (-1) = 3
                max_diff = min_diff = 0
				
				# diff at the previous occurance of c1/c2
                last_c1_diff = last_c2_diff = 0 
				
				# check wether we have met c1/c2 during the loop
                meet_c1 = meet_c2 = False
				
                for c in s:
                    if c == c1:
                        meet_c1 = True
                        diff += 1
						
						#  use last_c1_diff instead of diff because we have to make sure that c1 is in the rest part of the substring. 
						# e.g. [c1, c1, c2, c2, c2]
						# At index = 1, if we use diff = 2 -> max_diff = 2
						# At index = 4, diff = 2 - 3 = -1, result = max_diff - diff = 3. 
						# Though we have [c2, c2, c2] as a substring, c1 is not in this string and the result is invalid
                        max_diff = max(last_c1_diff, max_diff)
						
                        last_c1_diff = diff
                    elif c == c2:
                        meet_c2 = True
                        diff -= 1
                        min_diff = min(last_c2_diff, min_diff)
                        last_c2_diff = diff
                    else:
                        continue
					
					# update the result only when we have met both c1 and c2 
                    if meet_c1 and meet_c2:
                        res = max(diff - min_diff, max_diff - diff, res)
        return res
                        
        
        """
        counter = {}
        def getVariance(sub):
            if sub in dp:
                return dp[sub]
            max_value = max(counter.values())
            min_value = min(counter.values())
            dp[sub] = max_value - min_value
            return max_value - min_value
        
        dp = {}
        var = float("-inf")
        for i in range(len(s)):
            counter.clear()
            for j in range(i, len(s)):
                sub = s[i:j+1]
                counter[s[j]] = counter.get(s[j], 0) + 1
                var = max(var, getVariance(sub))
        return var
        """