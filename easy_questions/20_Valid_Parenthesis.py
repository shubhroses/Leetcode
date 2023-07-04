class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif c == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
            elif c == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack

class Solution:
    def isValid(self, string: str) -> bool:
        """ 
        string = "()[]"
                     c
        s = 
        top = [

        """
        s = []
        for c in string:
            if c in ['{', '[', '(']:
                s.append(c)
            else:
                if not s:
                    return False
                top = s.pop()
                if top == '{':
                    if c != '}':
                        return False
                if top == '(':
                    if c != ')':
                        return False
                if top == '[':
                    if c != ']':
                        return False
        if s:
            return False
        return True