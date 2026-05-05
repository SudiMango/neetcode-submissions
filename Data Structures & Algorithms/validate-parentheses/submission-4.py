class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                isEmpty = not bool(stack)
                if not isEmpty:
                    if c == ")" and stack[-1] == "(":
                        stack.pop()
                    elif c == "]" and stack[-1] == "[":
                        stack.pop()
                    elif c == "}" and stack[-1] == "{":
                        stack.pop()
                    else:
                        stack.append(c)
                else:
                    stack.append(c)
        
        return not bool(stack)

