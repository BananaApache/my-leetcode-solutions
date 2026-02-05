class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # edge case
        if len(position) == 1: # number of cars is 1
            return 1

        stack = []
        pairs = sorted([(p, s) for p, s in zip(position, speed)])
        
        for index in range(len(pairs) - 1, -1, -1):
            p, s = pairs[index]
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


