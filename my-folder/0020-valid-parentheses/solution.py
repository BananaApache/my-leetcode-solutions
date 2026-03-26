class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        charMap = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            # opening bracket
            if char not in charMap:
                stack.append(char)
            # closing bracket
            else:
                if not stack or stack[-1] != charMap[char]:
                    return False
                stack.pop()
        
        return len(stack) == 0

