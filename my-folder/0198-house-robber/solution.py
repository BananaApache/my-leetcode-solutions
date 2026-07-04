class Solution:
    def rob(self, nums: List[int]) -> int:

        # edge case
        if len(nums) == 1:
            return nums[0]
        
        dp = [0 for _ in range(len(nums))]
        dp[-1] = nums[-1]
        dp.append(0)

        for index in range(len(nums) - 2, -1, -1):
            dp[index] = max(nums[index] + dp[index + 2], dp[index + 1])
            
        return max(dp[0], dp[1])


