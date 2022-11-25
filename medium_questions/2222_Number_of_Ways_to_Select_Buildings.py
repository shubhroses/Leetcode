class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        want to select 3 elements from s, but not select any consecutive same elemnts 
        
        What if we converted all duplicates into single character. Then figure out how mnay 3 element arrays we can create 
        
        "0101"
        {0: 2,
         1: 2,
         0: 1,
         1: 1}
         
         2*2*3
         
         111000111000
         
         0101
         
         [(1, 3), (0, 2), (1, 3), (0, 3)]

        """
        dp = {"0": 0, "1": 0, "01": 0, "10": 0, "010": 0, "101": 0}
        for i in range(len(s)):
            if s[i] == "0":
                dp["0"] += 1
                dp["10"] += dp["1"]
                dp["010"] += dp["01"]
            if s[i] == "1":
                dp["1"] += 1
                dp["01"] += dp["0"]
                dp["101"] += dp["10"]
                
        return dp["010"] + dp["101"]
        """REsave""" 