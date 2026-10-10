class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        # [15 15 20  0  0 ]         
        # [10,15,20       ]

        dp = [0] * (len(cost) + 2)

        for index in range(len(cost) - 1, -1, -1):
            dp[index] = cost[index] + min(dp[index + 1], dp[index + 2])
        return min(dp[0], dp[1])

