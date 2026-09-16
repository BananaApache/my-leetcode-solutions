class Solution:
    def isValid(self, s: str) -> bool:
        
        close2open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for char in s:
            if char in close2open:
                if stack and stack[-1] == close2open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0

