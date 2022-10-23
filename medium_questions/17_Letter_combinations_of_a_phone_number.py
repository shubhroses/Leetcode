class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Each number could be 3-4 letter
        Matntain result array
        
        if len of letters same and length of digits add to result
        
        for each number iterate through each possible letter
        """
        numToChr = {"2": ['a', 'b', 'c'],
                    "3": ['d', 'e', 'f'],
                    "4": ['g', 'h', 'i'],
                    "5": ['j', 'k', 'l'],
                    "6": ['m', 'n', 'o'],
                    "7": ['p', 'q', 'r', 's'],
                    "8": ['t', 'u', 'v'],
                    "9": ['w', 'x', 'y', 'z']}
        
        if not digits:
            return []
        res = []
        
        def helper(i, curStr):
            if i == len(digits):
                res.append(curStr)
                return
                
            num = digits[i]
            for letter in numToChr[num]:
                helper(i+1, curStr + letter)
            
            
        helper(0, "")
        return res