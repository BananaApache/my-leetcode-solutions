class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        symbols = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        s = list(s)

        for char in s:
            if char in symbols.keys():
                stack.append(char)

            if char in symbols.values():
                if len(stack) > 0 and char == symbols[stack[-1]]:
                    stack.pop()
                else:
                    return False

        print(stack)

        if len(stack) != 0:
            return False
        else:
            return True
