class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for ch in tokens:
            if ch == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(x * y)
            elif ch == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x + y)
            elif ch == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y - x)
            elif ch == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(ch))
        return stack.pop()
                