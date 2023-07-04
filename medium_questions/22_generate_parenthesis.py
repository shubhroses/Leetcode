class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        helper with open and closed count
        
        if open == 0 and closed == 0:
            add to res
        if open == 0:
            close
        if open < close:
            open or close
        
        """
        
        res = []
        
        def helper(open_count, close_count, cur_str):
            if open_count < 0 or close_count < 0:
                return
            if open_count == 0 and close_count == 0:
                res.append(cur_str)
            elif open_count <= close_count:
                helper(open_count-1, close_count, cur_str + '(')
                helper(open_count, close_count-1, cur_str + ')')

        helper(n, n, "")
        return res
    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        o = 3
        c = 3

        res = []

        def helper(o, c, curStr):
            if o == 0 and c == 0:
                res.append(curStr)
                return 
            if o == c:
                helper(o-1, c, curStr + "(")
                return 
            # Take open
            helper(o-1, c, curStr + "(")

            # Take closed
            helper(o, c-1, curStr + ")")
        
        helper(n, n, "")
        """
        res = []

        def helper(o, c, curStr):
            if o < 0 or c < 0:
                return
            if c == 0:
                res.append(curStr)
                return 
            if o == c:
                helper(o-1, c, curStr + "(")
                return 
            # Take open
            helper(o-1, c, curStr + "(")

            # Take closed
            helper(o, c-1, curStr + ")")
        
        helper(n, n, "")
        return res