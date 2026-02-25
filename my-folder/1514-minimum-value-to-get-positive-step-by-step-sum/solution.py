class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        steps = []

        for num in nums:
            if not steps:
                steps.append(num)
            else:
                steps.append(steps[-1] + num)

        minSteps = min(steps)

        return max(1, 1 - minSteps)


