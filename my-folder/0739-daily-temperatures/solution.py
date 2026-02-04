class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures)
        stack = []
        
        #  0  1  2  3  4  5  6  7
        # [73,74,75,71,69,72,76,73]
        # [75 72 
        # timesPopped = 1
        # currentIndex = 6
        # [1, 1, 0, 2, 1, 1, 0, 0]

        # for each temperature
        for index in range(len(temperatures)):
            # while len(stack) != 0 and temperature > stack[-1]
            while len(stack) != 0 and temperatures[index] > stack[-1][0]:
                # currentIndex - timesPopped is the index in answer array
                poppedTemperature, poppedIndex = stack.pop()
                answer[poppedIndex] = index - poppedIndex
            
            stack.append((temperatures[index], index))

        return answer

