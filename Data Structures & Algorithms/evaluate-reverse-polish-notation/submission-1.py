class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            try:
                stack.append(int(t))
            except ValueError:
                b = stack.pop()
                a = stack.pop()
                operation = t
                stack.append(self._doCalc(a, b, operation))

        return stack[-1]

    def _doCalc(self, a, b, operation) -> int:
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        else:
            return int(a / b)
