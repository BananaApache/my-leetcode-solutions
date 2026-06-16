class Solution:
    def rob(self, nums: List[int]) -> int:

        # base cases
        if len(nums) < 3:
            return max(nums)
        
        nums.append(0)

        for index in range(len(nums) - 3, -1, -1):
            newCost = 0
            for cost in nums[index + 2 : ]:
                newCost = max(newCost, cost)

            nums[index] += newCost

        return max(nums[0], nums[1])

