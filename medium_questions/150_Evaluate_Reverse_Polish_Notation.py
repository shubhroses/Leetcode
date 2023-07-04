class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        maintain a stack
        for any number append to stack
        for any operator pop last two from stack and push result back onto stack

        def helper(a, b, o):
            a = int(a)
            b = int(b)
            if o == "+":
                return a + b
            if o == "-":
                return a - b
            if o == "*":
                return a * b
            if o == "/":
                return a//b

        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()
                new = str(helper(a, b, token))
                stack.append(new)
            else:
                stack.append(token)
        return int(stack[-1])

        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
                   t
        stack = [-237, 17]
        """
        def helper(a, b, o):
            a = int(a)
            b = int(b)
            if o == "+":
                return a + b
            if o == "-":
                return a - b
            if o == "*":
                return a * b
            if o == "/":
                if a / b < 0:
                    return math.ceil(a/b)
                else:
                    return a//b

        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()
                new = str(helper(a, b, token))
                stack.append(new)
            else:
                stack.append(token)
        return int(stack[-1])