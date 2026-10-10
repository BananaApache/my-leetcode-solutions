class Solution:
    def rob(self, nums: list[int]) -> int:

        #  [ 4  3  3  1  0  0 ]        
        #  [ 1  2  3  1       ]
        # choice at each house is max of (steal and take of index + 2, or skip and take index + 1)

        dp = [0] * (len(nums) + 2)
        for index in range(len(nums) - 1, -1, -1):
            dp[index] = max(nums[index] + dp[index + 2], dp[index + 1])
        return dp[0]

