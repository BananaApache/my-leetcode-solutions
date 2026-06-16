class Solution:
    def processStr(self, s: str) -> str:
        
        stack = ""

        for char in s:
            if char == '*':
                stack = stack[:-1]
            elif char == '#':
                stack += stack
            elif char == '%':
                stack = stack[::-1]
            else:
                stack += char

        return stack

