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