class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque();
        for ch in s:
            if ch == '}' and stack:
                ch2 = stack.pop()
                if ch2 != '{':
                    return False
            elif ch == ']' and stack:
                ch2 = stack.pop()
                if ch2 != '[':
                    return False
            elif ch == ')' and stack:
                ch2 = stack.pop()
                if ch2 != '(':
                    return False
            else:
                stack.append(ch)
        return not stack