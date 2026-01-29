class Solution:
    def isValid(self, s: str) -> bool:

        # edge case:
        if len(s) == 1:
            return False

        # ({[]})

        # (
        # popped = {

        # {{(
        # 
        
        # initializing
        stack = []

        bracketMap = {
            "]": "[", 
            ")": "(", 
            "}": "{"
        }

        # loop through entire string
        for index in range(len(s)):
            # if current char is "[" or "(" or "{" -> current char is a left bracket
            if s[index] in "[({":
                # append to stack
                stack.append(s[index])
            # else -> current char is a right bracket
            else:
                if len(stack) == 0:
                    return False
                # pop from stack
                popped = stack.pop()
                # if popped is not the opposite of current bracket
                if popped != bracketMap[s[index]]:
                    return False
        
        # if stack not empty
        if len(stack) != 0:
            return False
        else:
            return True

