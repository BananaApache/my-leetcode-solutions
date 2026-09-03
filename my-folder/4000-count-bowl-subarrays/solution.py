class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        
        stack = [nums[0]]
        result = 0
        for index in range(1, len(nums)):
            num = nums[index]
            while stack and stack[-1] < num:
                if len(stack) >= 2:
                    result += 1
                popped = stack.pop()
            
            stack.append(num)
        return result
