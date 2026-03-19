class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # [73,74,75,71,69,72,76,73]
        #                 

        #                 

        result = [0] * len(temperatures)
        stack = [] # max of stack should always be at bottom

        # loop through
        for index in range(len(temperatures)):
            # check new temp larger than top of stack
            while stack and temperatures[index] > stack[-1][0]: # stop when temp less than top of stack
                _, resultIndex = stack.pop()
                result[resultIndex] = index - resultIndex

            stack.append([temperatures[index], index])

        return result

