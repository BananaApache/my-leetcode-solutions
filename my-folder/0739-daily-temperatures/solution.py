class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # monotonic stack because used to keep track of larger ones by order
        # allows for iterative solution

        answer = [0 for _ in range(len(temperatures))]
        stack = [] # (index, temp)

        for index in range(len(temperatures)):
            if stack:
                while stack and stack[-1][1] < temperatures[index]:
                    poppedIndex, _ = stack.pop()
                    answer[poppedIndex] = index - poppedIndex

            stack.append( (index, temperatures[index]) )

        return answer

