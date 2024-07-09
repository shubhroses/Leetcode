class Solution:
    def validStrings(self, n: int) -> List[str]:
        """
        All substrings of x of length 2 contain at least one "1"
        
        At each index can select a 0 or 1
        if previous is 0 then can only select 1


        n = 3
        prevZero = False
        i = 0

        cur = "1", "0", 
            "11" "10" "01"
            "111" "110" "101" "010" "011"
        """

        self.res = []

        def helper(i, prevZero, cur):
            if i == n:
                self.res.append(cur)
                return
            
            if prevZero:
                helper(i+1, False, cur + "1")
                return
            if not cur:
                helper(i+1, False, "1")
                helper(i+1, True, "0")
            else:
                helper(i+1, False, cur + "1")
                helper(i+1, True, cur + "0")

        
        helper(0, False, "")
        return self.res


        
