class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # edge cases
        # length 1? [1] -> 1
        if len(tokens) == 1:
            return int(tokens[0])
        # length 2? [1, +] -> ?, [1, 2] -> ?

        operators = {'+', '-', '*', '/'}
        stack = []

        # [2, 1, + , 3, *]
        # [9

        for char in tokens:
            if char not in operators: # token is a number
                stack.append(int(char))
            else: # token is an operator
                rightNum = stack.pop()
                leftNum = stack.pop()

                if char == '+':
                    stack.append(leftNum + rightNum)
                elif char == '-':
                    stack.append(leftNum - rightNum)
                elif char == '*':
                    stack.append(leftNum * rightNum)
                elif char == '/':
                    stack.append(int(leftNum / rightNum))

        return stack[0]

